$(document).ready(function() {
  // Function to fetch and display the translation
  function fetchTranslation() {
    // Get the language code from the input field
    var langCode = $('#language_code').val();

    // Fetch the translation from the API
    $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
      // Display the translation in the DIV#hello
      $('#hello').text(data.hello);
    });
  }

  // Click event for the Translate button
  $('#btn_translate').click(function() {
    fetchTranslation();
  });

  // Keypress event for the input field
  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // ENTER key
      fetchTranslation();
    }
  });
});

