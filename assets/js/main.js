$(document).ready(function() {

  // Load the XML data
  $.get("lang_examples.xml", function (xml_data) {
    console.log("Loading data from lang_examples.xml ...");
    let header_table_row_template = $('#header-lang-table .row.template');
    let featureSections = $('#feature-sections');
    let sectionTemplate = $('#template-section');
    let pageNav = $('#page-nav-features');
    let pageNavTemplate = $('#page-nav-features .template');
    $(xml_data).find('feature').each(function(){
      let feature_node = $(this);
      let feature_name = feature_node.attr('name');
      console.log("Adding Language Feature ... " + feature_name);
      let feature_short_name = feature_name;
      if (feature_node.attr('short_name')) {
        feature_short_name = feature_node.attr('short_name');
        console.log("  Short Name: " + feature_short_name);
      }
      let sectionId = feature_short_name + '-section';
      let sectionTitleId = feature_short_name;
      
      // Create a new row in the header table
      let header_table_row = header_table_row_template.clone();
      header_table_row.appendTo('#header-lang-table');
      header_table_row.find('.feature-name a').html(feature_name + ':').attr('href', '#' + sectionId);
      let langList = header_table_row.find('.lang-list');
      let langListTemplate = langList.find('a');
      
      // Add to the page navigation
      pageNavTemplate.clone().appendTo(pageNav).removeClass('template').find('a').attr('href', '#' + sectionId).html(feature_short_name);
      
      // Create a new feature section
      let newSection = sectionTemplate.clone().attr('id', sectionId).appendTo(featureSections);
      newSection.find('.section-title').attr('id', sectionTitleId).html(feature_name);
      let exampleRowTemplate = newSection.find('.lang-example-row');
      
      feature_node.find('example').each(function(){
        let example_node = $(this);
        let exampleRow = exampleRowTemplate.clone().appendTo(newSection);
        let langTitleList = exampleRow.find('.lang-titles');
        let langTitleTemplate = langTitleList.find('.lang-title');
        let codeId = '';
        console.log("  Adding code example for these languages:")
        // Add each of the languages to the header table and the 1st column of the example row
        example_node.find('lang').each(function(){
          let xmlLangNode = $(this);
          let langName = xmlLangNode.attr('name');
          let langShortName = langName;
          if (xmlLangNode.attr('short_name')) {
            langShortName = xmlLangNode.attr('short_name');
          }
          console.log("    " + langName)
          let langNameSanitized = langName.replace(/[+ ]/g, function (m) {
            // Replace any characters that aren't safe for CSS and HTML
            return {
              '+': 'p',
              ' ': '_',
              // If you come across more characters that need to be replaced, add them here and in the regex above
            }[m];
          });
          let langLink = xmlLangNode.attr('link');
          if (codeId === '') {  // We make the code ID the first lang
            codeId = feature_short_name + '-' + langNameSanitized + '-code';
          }
          if (xmlLangNode.attr('display_in_table') === undefined || xmlLangNode.attr('display_in_table') !== 'false') {
            langListTemplate.clone().attr('href', '#' + codeId).html(langShortName).appendTo(langList);
          }
          langTitleTemplate.clone().attr('id', feature_short_name + '-' + langNameSanitized).appendTo(langTitleList).find('a').attr('href', langLink).html(langName);
        });
        langTitleTemplate.detach();  // Remove the empty template item
        // Add the code, removing any whitespace from beginning and end
        exampleRow.find('code').attr('id', codeId).html(example_node.find('code').html().replace(/^\n+|\s+$/g, ''));
        exampleRow.find('.clipboard-copy').attr('data-clipboard-target', '#' + codeId)
      });
      
      // Cleanup
      langListTemplate.detach();  // Remove the empty template item
      exampleRowTemplate.detach();
      header_table_row.removeClass('template');
      newSection.removeClass('template');
    });
	
	  /* ======= Fixed page nav when scrolled ======= */    
    $(window).on('scroll resize load', function() {
        
        $('#page-nav-wrapper').removeClass('fixed');
         
         var scrollTop = $(this).scrollTop();
         var topDistance = $('#page-nav-wrapper').offset().top;
         
         if ( (topDistance) > scrollTop ) {
            $('#page-nav-wrapper').removeClass('fixed');
            $('body').removeClass('sticky-page-nav');
         }
         else {
            $('#page-nav-wrapper').addClass('fixed');
            $('body').addClass('sticky-page-nav');
         }

    });
    
    new Clipboard('.clipboard-copy');
    hljs.initHighlighting();
    $('.clipboard-copy').prop('title', 'Copy to Clipboard').tooltip();

    $('.linkable').each(function() {
        let e = $(this);
        let eId = e.attr('id');
        if (e.prop('tagName') == "A") {
            e.after(
                '<a id="' + eId + 'LinkButton" class="headerlink" style="opacity:0" href="#' + eId + '" title="Permalink to this headline">¶</a><a class="offsetAnchor" id="' + eId + '"></a>'
            );
        } else {
            e.append(
                '<a id="' + eId + 'LinkButton" class="headerlink" style="opacity:0" href="#' + eId + '" title="Permalink to this headline">¶</a><a class="offsetAnchor" id="' + eId + '"></a>'
            );
        }
        e.attr('id', eId + 'Text').hover(
            function() {  // Mouse Enter
                $('#' + eId + 'LinkButton').css('opacity', 1);
            },
            function() {  // Mouse Exit
                $('#' + eId + 'LinkButton').css('opacity', '0');
            }
        );
    });
  
    /* ======= Scrollspy ======= */
    $('body').scrollspy({ target: '#page-nav-wrapper', offset: 100});
    /* ======= ScrollTo ======= */
    $('.scrollto').on('click', function(e){
      //store hash
      var target = this.hash;
      e.preventDefault();
  		$('body').scrollTo(target, 800, {offset: -60, axis:'y'});
  	});

  }).fail(function(jqXHR, textStatus, errorThrown) {
    console.log("There was an error loading lang_examples.xml: " + textStatus + " " + errorThrown);
  });
    

});