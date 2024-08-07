$(document).ready(function() {
  $('#btn_translate').click(function() {
    // Get the language code from the input field
    var langCode = $('#language_code').val();

    // Fetch the translation from the API
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
      // Display the translation in the DIV#hello
      $('#hello').text(data.hello);
    });
  });
});
