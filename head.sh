#!/bin/bash
$fsweb visitor.jpg
$cd/home/pi
$convert visitor.jpg visitor.png
$rm visitor.jpg
$mv visitor.png /home/pi/Desktop/scanner
$cd /home/pi/Desktop/scanner
$./.py