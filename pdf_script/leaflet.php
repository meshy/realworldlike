<?php

// Can be downloaded from http://www.fpdf.org/
require("fpdf17/fpdf.php");

function GetPage($url="http://www.example.com/") {
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_FRESH_CONNECT, TRUE);
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 5);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, TRUE);
    curl_setopt($ch, CURLOPT_TIMEOUT, 10);
    $html = curl_exec($ch);
    if ($html == false) {
        $m = curl_error(($ch));
        error_log($m);
    }
    curl_close($ch);
    return $html;
}

function GeneratePDF($background, $backgroundtype, $posx, $posy, $size, $number, $code, $objectids) {
    if ($size < 30) {
        return false;
    }

    $pdf = new FPDF("P", "mm", "A4");

    $dimensions = $size . "x" . $size;

    for ($i = 0; $i < count($objectids); $i++) {
        $pdf->AddPage();

        if ($background != null) {
            $pdf->Image($background, 0, 0, $pdf->w, $pdf->h, $backgroundtype);
        }

        $qrstring = urlencode("smsto:$number:$code $objectids[$i]");

        $remoteFile = "http://chart.apis.google.com/chart?" .
                "chs=$dimensions&cht=qr&chld=L|0&chl=$qrstring";

        // Insert the QR Code
        $pdf->Image($remoteFile, $posx, $posy, $size, $size, 'png');

        // Insert the SMS number
        $pdf->SetFont("Helvetica");
        $pdf->SetFontSize(18);
        $width = $pdf->GetStringWidth("Text " . $number);
        $pdf->Text($posx - $width, $posy + 5, "Text " . $number);

        // Insert the SMS Code
        $width = $pdf->GetStringWidth("With " . $code . " " . $objectids[$i]);
        $pdf->Text($posx - $width - 1, $posy + 12, "With " . $code . " " . $objectids[$i]);

    }

    $name = date("Y-m-d-H-i-s");
    $pdf->Output($name, "I");
}

if (isset($_GET["printrunid"])) {
    // Request data from Database
    $databaseLink = "http://realworldlike.omnicronsoftware.com/";
    $printrun = "realworldlike/printrun/";
    $printrunID = $_GET["printrunid"];
    $jsonstring = GetPage($databaseLink . $printrun . $printrunID . "/");

    $json = json_decode($jsonstring, true);
    if ($json == NULL || $json == false) {
        echo "Invalid JSON";
        echo "<br /><br />";
        echo $jsonstring;
        return false;
    }

    $background = "http://omnicronsoftware.com/hackspace/A3_Robin_Hood_Tax-Campaign-poster.jpg";
    $fileType = "jpg";

    $codes = $json["poster_ids"];
    $left = $json["qr"]["left"];
    $top = $json["qr"]["top"];
    $size = $json["qr"]["size"];
    $phoneNum = $json["campaign"]["number"];
    $campaignCode = $json["campaign"]["keyword"];

    GeneratePDF($background, $fileType, $left, $top, $size, $phoneNum, $campaignCode, $codes);
}

//210x 300y
?>