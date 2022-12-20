# JPEG Polyglot Generator

## Polyglot?

A file that's valid in multiple different formats. In our example, JPEG & JS.

## Description

A simple script to add a JavaScript code in a JPEG file. The file is both a valid JPEG image and a valid JS file using 'ISO-8859-1' encoding. JS Payload is stored in comment section of the JPEG image.

Image can be used for XSS Attack using 

```html
<script charset="ISO-8859-1" src="./output.jpg"></script>
```

Reference: [PortSwigger](https://portswigger.net/research/bypassing-csp-using-polyglot-jpegs)
