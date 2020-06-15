from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'username': 'timothy.slade@gmail.com',
    'password': 'CostaConcordia2014',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
    # 'cookiefile': '~/projects/audiosetdl/tslade-cookies.txt'
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])


# from bs4 import BeautifulSoup
# import urllib2

# url = "https://www.engageny.org/content/nysut-rubric-teacher-selects-appropriate-curricular-materials-and-resources"

# urllib.urlopen

# content = urllib.urlopen(url).read()

# soup = BeautifulSoup(content)

# print(soup.prettify())

# print(title)

# print(soup.title.string)

# print(soup.p)


# <!DOCTYPE html>
# <html dir="ltr" lang="en">
#  <head>
#   <link href="http://www.w3.org/1999/xhtml/vocab" rel="profile"/>
#   <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
#   <!--[if IE]><![endif]-->
#   <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
#    <meta content="Drupal 7 (http://drupal.org)" name="Generator"/>
#    <link href="/content/nysut-rubric-teacher-selects-appropriate-curricular-materials-and-resources" rel="canonical"/>
#    <link href="/node/40756" rel="shortlink"/>
#    <meta content="NYSUT Rubric: Teacher Selects Appropriate Curricular Materials and Resources" property="og:title"/>
#    <meta content="These videos&amp;amp;nbsp;of exemplary teacher practice are aligned to:

# NYSUT&amp;amp;rsquo;s Teacher Practice Rubric


#     Standard II: Knowledge of Content and Instructional Planning
        
#             Element II.6: Teache" property="og:description"/>
#    <meta content="https://www.engageny.org/sites/all/themes/eny_subtheme/default_image.jpg" property="og:image"/>
#    <meta content="https://www.engageny.org/content/nysut-rubric-teacher-selects-appropriate-curricular-materials-and-resources" property="og:url"/>
#    <meta content="EngageNY" property="og:site_name"/>
#    <link href="https://www.engageny.org/sites/all/themes/eny_subtheme/favicon.ico" rel="shortcut icon" type="image/vnd.microsoft.icon"/>
#    <meta content="1592010636" property="og:updated_time"/>
#    <meta content="https://www.engageny.org/sites/default/files/media-youtube/V_FdG4sy614.jpg" property="og:image"/>
#    <title>
#     NYSUT Rubric: Teacher Selects Appropriate Curricular Materials and Resources | EngageNY
#    </title>
#    <link href="/sites/default/files/advagg_css/css__cP9z55tqzFmUEmhGay4lnbdjIaRmw6JIHfHuoT9JT8I__LbMjengOTvfkl1rqbHCcztxx-T-HDqphiiohzRkDRGI__ENQm_6H-iTBcm2G6yrSzwAbhe4gKYe46HYukHKmJLOo.css" media="all" rel="stylesheet" type="text/css"/>
#    <link href="//fonts.googleapis.com/css?family=Open+Sans" media="all" rel="stylesheet" type="text/css"/>
#    <link href="/sites/default/files/advagg_css/css__tzaiYWBrVRRZMmrOeEJiFAwexBqC5Fp8Y9UeVPGHJLM__-li-YxkXTX-Jljflic9ZW2CvDG_0mS0C0a1DAuMTyDY__ENQm_6H-iTBcm2G6yrSzwAbhe4gKYe46HYukHKmJLOo.css" media="all" rel="stylesheet" type="text/css"/>
#    <link href="/sites/default/files/advagg_css/css__mJwESta2O_Uei91eIosgfhCb8SFFobkrrJPr1unvinQ__e7moDGm6OEZK9OumPhp80gewZIPtYebJDCevi7rAgbM__ENQm_6H-iTBcm2G6yrSzwAbhe4gKYe46HYukHKmJLOo.css" media="all" rel="stylesheet" type="text/css"/>
#    <!-- HTML5 element support for IE6-8 -->
#    <!--[if lt IE 9]>
#     <script src="https://cdn.jsdelivr.net/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
#   <![endif]-->
#    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js" type="text/javascript">
#    </script>
#    <script type="text/javascript">
#     <!--//--><![CDATA[//><!--
# window.jQuery || document.write("<script src='/sites/all/modules/contrib/jquery_update/replace/jquery/1.10/jquery.min.js'>\x3C/script>")
# //--><!]]>
#    </script>
#    <script src="/sites/default/files/advagg_js/js__LJ_NYZGWp-JD3yakbYNSUrTCBrTjvN4YM44Uk_vlA_g__H9_Fn4lh3aYzVkTAIJSipssyr5y4yEkU4SN3zv5QVD4__ENQm_6H-iTBcm2G6yrSzwAbhe4gKYe46HYukHKmJLOo.js" type="text/javascript">
#    </script>
#    <script type="text/javascript">
#     <!--//--><![CDATA[//><!--
# (function(i,s,o,g,r,a,m){i["GoogleAnalyticsObject"]=r;i[r]=i[r]||function(){(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)})(window,document,"script","https://www.google-analytics.com/analytics.js","ga");ga("create", "UA-24843998-1", {"cookieDomain":".engageny.org"});ga("send", "pageview");
# //--><!]]>
#    </script>
#    <script src="/sites/default/files/advagg_js/js__F24SlCvfmpHiNpKOzxTJMB1H9JdthxCb5daQFHvkRhQ__jgMbeVQOEiVWM42Z6BSYezeEeI0pNkQ-kUAitWZAFTg__ENQm_6H-iTBcm2G6yrSzwAbhe4gKYe46HYukHKmJLOo.js" type="text/javascript">
#    </script>
#    <script type="text/javascript">
#     <!--//--><![CDATA[//><!--
# jQuery.extend(Drupal.settings, {"basePath":"\/","pathPrefix":"","ajaxPageState":{"theme":"eny_subtheme","theme_token":"rz-fKdt8L2bf25k4oMyrb4T5Du-KvlTikbeAyAvoFpI","jquery_version":"1.10","css":{"modules\/system\/system.base.css":1,"sites\/all\/modules\/contrib\/date\/date_api\/date.css":1,"sites\/all\/modules\/contrib\/date\/date_popup\/themes\/datepicker.1.7.css":1,"modules\/field\/theme\/field.css":1,"sites\/all\/modules\/contrib\/logintoboggan\/logintoboggan.css":1,"modules\/node\/node.css":1,"sites\/all\/modules\/custom\/nysed_help\/css\/nysed_help.css":1,"sites\/all\/modules\/custom\/nysed_site_survey\/templates\/nysed-survey.css":1,"sites\/all\/modules\/contrib\/extlink\/extlink.css":1,"sites\/all\/modules\/contrib\/views\/css\/views.css":1,"sites\/all\/modules\/contrib\/ctools\/css\/ctools.css":1,"sites\/all\/modules\/patched\/panels\/css\/panels.css":1,"sites\/all\/modules\/contrib\/popup\/popup.css":1,"sites\/all\/modules\/patched\/rate\/rate.css":1,"sites\/all\/modules\/contrib\/print\/print_ui\/css\/print_ui.theme.css":1,"sites\/all\/libraries\/slick\/slick\/slick.css":1,"sites\/all\/modules\/custom\/nysed_rate\/templates\/nysed_like\/nysed_like.css":1,"\/\/fonts.googleapis.com\/css?family=Open+Sans":1,"sites\/all\/libraries\/superfish\/css\/superfish.css":1,"sites\/all\/libraries\/superfish\/css\/superfish-smallscreen.css":1,"sites\/all\/themes\/eny_subtheme\/css\/font-awesome.min.css":1,"sites\/all\/themes\/eny_subtheme\/css\/core.css":1,"sites\/all\/themes\/eny_subtheme\/https:\/\/maxcdn.bootstrapcdn.com\/bootstrap\/3.3.4\/css\/bootstrap.min.css":1},"js":{"\/\/s7.addthis.com\/js\/300\/addthis_widget.js#pubid=ra-556caa5d37346a5e":1,"sites\/all\/themes\/bootstrap\/js\/bootstrap.js":1,"\/\/ajax.googleapis.com\/ajax\/libs\/jquery\/1.10.2\/jquery.min.js":1,"misc\/jquery-extend-3.4.0.js":1,"misc\/jquery-html-prefilter-3.5.0-backport.js":1,"misc\/jquery.once.js":1,"misc\/drupal.js":1,"sites\/all\/libraries\/balupton-history.js\/scripts\/bundled\/html4+html5\/jquery.history.js":1,"sites\/all\/modules\/contrib\/jquery_update\/replace\/ui\/external\/jquery.cookie.js":1,"sites\/all\/modules\/contrib\/jquery_update\/replace\/misc\/jquery.form.min.js":1,"sites\/all\/libraries\/bxslider\/jquery.bxslider.min.js":1,"misc\/ajax.js":1,"sites\/all\/modules\/contrib\/jquery_update\/js\/jquery_update.js":1,"sites\/all\/modules\/contrib\/extlink\/extlink.js":1,"sites\/all\/modules\/contrib\/popup\/popup.js":1,"sites\/all\/modules\/contrib\/views\/js\/base.js":1,"sites\/all\/themes\/bootstrap\/js\/misc\/_progress.js":1,"sites\/all\/modules\/contrib\/views\/js\/ajax_view.js":1,"sites\/all\/modules\/custom\/nysed_books\/videos.js":1,"sites\/all\/themes\/eny_subtheme\/js\/jquery.matchHeight.js":1,"sites\/all\/libraries\/slick\/slick\/slick.min.js":1,"sites\/all\/modules\/custom\/nysed_content_types\/nysed_ct_video_album\/js\/nysed_ct_video_album.js":1,"sites\/all\/modules\/custom\/nysed_content_types\/nysed_ct_video\/js\/jquery.jsonp.js":1,"sites\/all\/modules\/custom\/nysed_content_types\/nysed_ct_video\/js\/nysed_ct_video.js":1,"sites\/all\/modules\/custom\/nysed_rate\/js\/nysed_rate.js":1,"sites\/all\/modules\/patched\/rate\/rate.js":1,"sites\/all\/modules\/contrib\/google_analytics\/googleanalytics.js":1,"sites\/all\/libraries\/superfish\/jquery.hoverIntent.minified.js":1,"sites\/all\/libraries\/superfish\/sftouchscreen.js":1,"sites\/all\/libraries\/superfish\/sfsmallscreen.js":1,"sites\/all\/libraries\/superfish\/supposition.js":1,"sites\/all\/libraries\/superfish\/superfish.js":1,"sites\/all\/libraries\/superfish\/supersubs.js":1,"sites\/all\/modules\/contrib\/superfish\/superfish.js":1,"sites\/all\/themes\/eny_subtheme\/js\/bootstrap.min.js":1,"sites\/all\/themes\/eny_subtheme\/js\/navbar.js":1,"sites\/all\/themes\/eny_subtheme\/js\/content.js":1,"sites\/all\/themes\/bootstrap\/js\/modules\/views\/js\/ajax_view.js":1,"sites\/all\/themes\/bootstrap\/js\/misc\/ajax.js":1}},"popup":{"effects":{"show":{"default":"this.body.show();","fade":"\n        if (this.opacity){\n          this.body.fadeTo(\u0027medium\u0027,this.opacity);\n        }else{\n          this.body.fadeIn(\u0027medium\u0027);\n        }","slide-down":"this.body.slideDown(\u0027medium\u0027)","slide-down-fade":"\n        this.body.animate(\n          {\n            height:\u0027show\u0027,\n            opacity:(this.opacity ? this.opacity : \u0027show\u0027)\n          }, \u0027medium\u0027\n        );"},"hide":{"default":"this.body.hide();","fade":"this.body.fadeOut(\u0027medium\u0027);","slide-down":"this.body.slideUp(\u0027medium\u0027);","slide-down-fade":"\n        this.body.animate(\n          {\n            height:\u0027hide\u0027,\n            opacity:\u0027hide\u0027\n          }, \u0027medium\u0027\n        );"}},"linger":"250","delay":"0"},"views":{"ajax_path":"\/views\/ajax","ajaxViews":{"views_dom_id:952da7e574232f2e7feb21502a8c19a7":{"view_name":"related_items","view_display_id":"block","view_args":"40756","view_path":"node\/40756","view_base_path":"resource\/!1\/related-resources","view_dom_id":"952da7e574232f2e7feb21502a8c19a7","pager_element":0}}},"urlIsAjaxTrusted":{"\/views\/ajax":true},"rate":{"basePath":"\/rate\/vote\/js","destination":"node\/40756"},"extlink":{"extTarget":"_blank","extClass":"ext","extLabel":"(link is external)","extImgClass":true,"extIconPlacement":"append","extSubdomains":1,"extExclude":"[a-z\\-]*\\.?(engageny\\.org|nysarchives\\.org|nysarchivestrust\\.org|nyshrab\\.org |nysed\\.gov|novelnewyork\\.org|nybiodiversity\\.org|nationalccrs\\.org|nysedregents\\.org|officeofprofessions\\.custhelp\\.com|formstack\\.com|search\\.its\\.ny\\.gov|onmytrack\\.com|datacation\\.net|schoolnet\\.com)","extInclude":"","extCssExclude":"","extCssExplicit":"","extAlert":"_blank","extAlertText":"You are exiting the EngageNY.org web site. The site you are about to visit is not under the jurisdiction of NYSED and NYSED is not responsible for its content. ","mailtoClass":"mailto","mailtoLabel":"(link sends e-mail)"},"googleanalytics":{"trackOutbound":1,"trackMailto":1,"trackDownload":1,"trackDownloadExtensions":"7z|aac|arc|arj|asf|asx|avi|bin|csv|docx?|exe|flv|gif|gz|gzip|hqx|jar|jpe?g|js|mp(2|3|4|e?g)|mov(ie)?|msi|msp|pdf|phps|png|pptx?|qtm?|ra(m|r)?|sea|sit|tar|tgz|torrent|txt|wav|wma|wmv|wpd|xlsx?|xml|z|zip","trackDomainMode":1,"trackCrossDomains":["acquia-sites.com","engageny.org"]},"superfish":{"1":{"id":"1","sf":{"animation":{"opacity":"show"},"speed":200,"dropShadows":false},"plugins":{"touchscreen":{"behaviour":"1","mode":"window_width","breakpoint":992,"breakpointUnit":"px"},"smallscreen":{"mode":"window_width","breakpoint":992,"breakpointUnit":"px","accordionButton":"2","title":"Main menu"},"supposition":true,"supersubs":{"minWidth":"17","maxWidth":"40"}}}},"bootstrap":{"anchorsFix":0,"anchorsSmoothScrolling":0,"formHasError":1,"popoverEnabled":1,"popoverOptions":{"animation":1,"html":0,"placement":"right","selector":"","trigger":"click","triggerAutoclose":1,"title":"","content":"","delay":0,"container":"body"},"tooltipEnabled":1,"tooltipOptions":{"animation":1,"html":0,"placement":"auto left","selector":"","trigger":"hover focus","delay":0,"container":"body"}}});
# //--><!]]>
#    </script>
#   </meta>
#  </head>
#  <body class="html not-front not-logged-in no-sidebars page-node page-node- page-node-40756 node-type-video-album">
#   <div id="skip-link">
#    <a class="element-invisible element-focusable" href="#main-content">
#     Skip to main content
#    </a>
#   </div>
#   <header class="site-header" id="navbar" role="banner">
#    <div class="container">
#     <div class="row">
#      <div class="col-xs-12 col-sm-12 col-md-2 header-left">
#       <a class="logo" href="/" title="Home">
#        <img alt="Home" src="https://www.engageny.org/sites/all/themes/eny_subtheme/logo.png"/>
#       </a>
#       <button aria-controls="navbar" aria-expanded="false" class="navbar-toggle collapsed" data-target="#menu-small-links" data-toggle="collapse" type="button">
#        <i aria-label="menu icon" class="fa fa-bars">
#        </i>
#        Extras
#       </button>
#       <a class="hidden-lg hidden-md" href="#" id="search-toggle" role="button">
#        <span class="sr-only">
#         Toggle search
#        </span>
#        <i aria-label="toggle search icon" class="fa fa-search-plus fa-spaced">
#        </i>
#       </a>
#      </div>
#      <!-- /.header-left -->
#      <div class="col-xs-12 col-sm-12 col-md-7 header-right">
#       <div class="navbar-collapse collapse" id="menu-small-links">
#        <!-- Use CSS to replace link text with flag icons -->
#        <div id="google_translate_element">
#        </div>
#        <script type="text/javascript">
#         function googleTranslateElementInit() {
#                             new google.translate.TranslateElement({pageLanguage: 'en', includedLanguages: 'ar,bn,de,el,en,es,fr,ht,hu,id,it,ja,pt,ru,sv,th,tl,tr,uk,yi,zh-CN,zh-TW', layout: google.translate.TranslateElement.InlineLayout.SIMPLE, gaTrack: true, gaId: 'UA-24843998-1'}, 'google_translate_element');
#                             jQuery('#goog-gt-tt img').attr('alt', 'Google translate Icon');
#                         }
#        </script>
#        <script src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit" type="text/javascript">
#        </script>
#        <ul class="nav navbar-nav small-links" id="menu-top-menu">
#         <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-62">
#          <a href="/resource/frequently-asked-questions-about-common-core-curriculum">
#           FAQ
#          </a>
#         </li>
#         <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-62">
#          <a href="#" onclick="showZendeskWidget()">
#           Help
#          </a>
#          <script id="ze-snippet" src="https://static.zdassets.com/ekr/snippet.js?key=5982dd0a-0aee-41d1-a421-ddf063266df9">
#          </script>
#          <script type="text/javascript">
#           zE('webWidget', 'hide'); 
#                                 function showZendeskWidget(){
#                                     zE('webWidget', 'show'); //you have to show then open
#                                     zE('webWidget', 'open');
#                                     }  
#                                 zE('webWidget:on', 'close', function() {
#                                     zE('webWidget', 'reset'); 
#                                     zE('webWidget', 'hide');   
#                                 });
#          </script>
#         </li>
#        </ul>
#       </div>
#      </div>
#      <div class="col-xs-12 col-sm-5 col-md-3 search-form hidden-xs hidden-sm" id="search-form">
#       <form action="/search-site" class="search_form" method="get" name="search_form">
#        <div class="input-group">
#         <input class="field_search form-control" name="search" placeholder="Search the site..." title="Search the site..." type="text"/>
#         <span class="input-group-btn">
#          <button class="btn btn-default" type="submit">
#           <span class="sr-only">
#            Search
#           </span>
#           <i aria-hidden="true" class="fa fa-search">
#           </i>
#          </button>
#         </span>
#        </div>
#       </form>
#      </div>
#     </div>
#    </div>
#    <div class="navbar-main">
#     <div class="container">
#      <div class="region region-navigation">
#       <section class="block block-superfish clearfix" id="block-superfish-1">
#        <nav class="main-navigation clearfix" id="main-menu">
#         <ul class="menu sf-menu sf-main-menu sf-horizontal sf-style-none sf-total-items-6 sf-parent-items-5 sf-single-items-1 menu nav navbar-nav" id="superfish-1">
#          <li class="first odd sf-item-1 sf-depth-1 leaf sf-no-children" id="menu-46386-1">
#           <a class="sf-depth-1" href="/next-generation-learning-standards" title="The New York State Next Generation Learning Standards">
#            Next Generation Learning Standards
#           </a>
#          </li>
#          <li class="middle even sf-item-2 sf-depth-1 leaf sf-total-children-10 sf-parent-children-2 sf-single-children-8 menuparent" id="menu-43126-1">
#           <a class="sf-depth-1 menuparent" href="/ccss-library">
#            Common Core
#           </a>
#           <ul>
#            <li class="first odd sf-item-1 sf-depth-2 leaf sf-no-children" id="menu-43396-1">
#             <a class="sf-depth-2" href="/ccss-library">
#              Common Core Library
#             </a>
#            </li>
#            <li class="middle even sf-item-2 sf-depth-2 leaf sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent" id="menu-43371-1">
#             <a class="sf-depth-2 menuparent" href="/resource/new-york-state-p-12-common-core-learning-standards">
#              Common Core Learning Standards
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43411-1">
#               <a class="sf-depth-3" href="/resource/new-york-state-prekindergarten-foundation-for-the-common-core">
#                New York State Prekindergarten Foundation for the Common Core
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43416-1">
#               <a class="sf-depth-3" href="/resource/new-york-state-p-12-common-core-learning-standards-for-english-language-arts-and-literacy">
#                Common Core Learning Standards for ELA
#               </a>
#              </li>
#              <li class="last odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43421-1">
#               <a class="sf-depth-3" href="/resource/new-york-state-p-12-common-core-learning-standards-for-mathematics">
#                Common Core Learning Standards for Mathematics
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="middle odd sf-item-3 sf-depth-2 leaf sf-no-children" id="menu-43376-1">
#             <a class="sf-depth-2" href="/resource/common-core-toolkit">
#              Common Core Implementation Resources
#             </a>
#            </li>
#            <li class="middle even sf-item-4 sf-depth-2 leaf sf-no-children" id="menu-43381-1">
#             <a class="sf-depth-2" href="/common-core-curriculum">
#              Common Core Curriculum
#             </a>
#            </li>
#            <li class="middle odd sf-item-5 sf-depth-2 leaf sf-no-children" id="menu-43406-1">
#             <a class="sf-depth-2" href="/resource/curriculum-module-updates">
#              Curriculum Module Updates
#             </a>
#            </li>
#            <li class="middle even sf-item-6 sf-depth-2 leaf sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent" id="menu-43401-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              Common Core Assessments
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43431-1">
#               <a class="sf-depth-3" href="/3-8">
#                Common Core 3-8 ELA and Mathematics Tests
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43426-1">
#               <a class="sf-depth-3" href="/resource/regents-exams">
#                Common Core Regents Exams
#               </a>
#              </li>
#              <li class="last odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43436-1">
#               <a class="sf-depth-3" href="/resource/new-york-state-english-a-second-language-achievement-test-nyseslat-resources">
#                NYSESLAT
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="middle odd sf-item-7 sf-depth-2 leaf sf-no-children" id="menu-43386-1">
#             <a class="sf-depth-2" href="/resource/new-york-state-bilingual-common-core-initiative">
#              Bilingual Common Core Initiative
#             </a>
#            </li>
#            <li class="middle even sf-item-8 sf-depth-2 leaf sf-no-children" id="menu-43391-1">
#             <a class="sf-depth-2" href="/new-york-state-k-12-social-studies">
#              Social Studies
#             </a>
#            </li>
#            <li class="middle odd sf-item-9 sf-depth-2 leaf sf-no-children" id="menu-45486-1">
#             <a class="sf-depth-2" href="/resource/high-school-equivalency-curriculum-framework">
#              High School Equivalency Curriculum Framework
#             </a>
#            </li>
#            <li class="last even sf-item-10 sf-depth-2 leaf sf-no-children" id="menu-46101-1">
#             <a class="sf-depth-2" href="/resource/tasc-transition-curriculum">
#              TASC Transition Curriculum
#             </a>
#            </li>
#           </ul>
#          </li>
#          <li class="middle odd sf-item-3 sf-depth-1 leaf sf-total-children-3 sf-parent-children-2 sf-single-children-1 menuparent" id="menu-43141-1">
#           <a class="sf-depth-1 menuparent" href="/tle-library">
#            Teacher/Leader Effectiveness
#           </a>
#           <ul>
#            <li class="first odd sf-item-1 sf-depth-2 leaf sf-no-children" id="menu-43511-1">
#             <a class="sf-depth-2" href="/tle-library">
#              Teacher/Leader Effectiveness Library
#             </a>
#            </li>
#            <li class="middle even sf-item-2 sf-depth-2 leaf sf-total-children-5 sf-parent-children-0 sf-single-children-5 menuparent" id="menu-43516-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              Evaluation
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43531-1">
#               <a class="sf-depth-3" href="/resource/appr-3012-c">
#                APPR (3012-c)
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43536-1">
#               <a class="sf-depth-3" href="/resource/appr-3012-d">
#                APPR (3012-d)
#               </a>
#              </li>
#              <li class="middle odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43541-1">
#               <a class="sf-depth-3" href="/resource/student-learning-objectives">
#                Student Learning Objectives
#               </a>
#              </li>
#              <li class="middle even sf-item-4 sf-depth-3 leaf sf-no-children" id="menu-43546-1">
#               <a class="sf-depth-3" href="/resource/resources-about-state-growth-measures">
#                State Growth Measures
#               </a>
#              </li>
#              <li class="last odd sf-item-5 sf-depth-3 leaf sf-no-children" id="menu-43551-1">
#               <a class="sf-depth-3" href="/resource/state-approved-tools">
#                State-Approved Tools
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="last odd sf-item-3 sf-depth-2 leaf sf-total-children-2 sf-parent-children-0 sf-single-children-2 menuparent" id="menu-43506-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              Improving Practice
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43526-1">
#               <a class="sf-depth-3" href="/resource/improving-practice">
#                Improving Practice
#               </a>
#              </li>
#              <li class="last even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43521-1">
#               <a class="sf-depth-3" href="/new-york-state-career-ladder-pathways-toolkit">
#                Career Ladder Pathways
#               </a>
#              </li>
#             </ul>
#            </li>
#           </ul>
#          </li>
#          <li class="middle even sf-item-4 sf-depth-1 leaf sf-total-children-4 sf-parent-children-0 sf-single-children-4 menuparent" id="menu-43116-1">
#           <a class="sf-depth-1 menuparent" href="/video-library">
#            Video Library
#           </a>
#           <ul>
#            <li class="first odd sf-item-1 sf-depth-2 leaf sf-no-children" id="menu-43326-1">
#             <a class="sf-depth-2" href="/video-library">
#              Video Library
#             </a>
#            </li>
#            <li class="middle even sf-item-2 sf-depth-2 leaf sf-no-children" id="menu-44046-1">
#             <a class="sf-depth-2" href="/content/danielsons-framework-teaching-rubric-videos">
#              Danielson’s Framework for Teaching Rubric Videos
#             </a>
#            </li>
#            <li class="middle odd sf-item-3 sf-depth-2 leaf sf-no-children" id="menu-44051-1">
#             <a class="sf-depth-2" href="/content/nysut-teacher-practice-rubric-videos">
#              NYSUT Teacher Practice Rubric Videos
#             </a>
#            </li>
#            <li class="last even sf-item-4 sf-depth-2 leaf sf-no-children" id="menu-43331-1">
#             <a class="sf-depth-2" href="/resource/video-professional-development-series">
#              Video Professional Development Series
#             </a>
#            </li>
#           </ul>
#          </li>
#          <li class="middle odd sf-item-5 sf-depth-1 leaf sf-total-children-10 sf-parent-children-5 sf-single-children-5 menuparent" id="menu-43111-1">
#           <a class="sf-depth-1 menuparent" href="/pdnt-library">
#            ﻿Professional Development
#           </a>
#           <ul>
#            <li class="first odd sf-item-1 sf-depth-2 leaf sf-no-children" id="menu-43181-1">
#             <a class="sf-depth-2" href="/pdnt-library">
#              Professional Development Library
#             </a>
#            </li>
#            <li class="middle even sf-item-2 sf-depth-2 leaf sf-no-children" id="menu-43186-1">
#             <a class="sf-depth-2" href="/resource/video-professional-development-series">
#              Video Professional Development Series
#             </a>
#            </li>
#            <li class="middle odd sf-item-3 sf-depth-2 leaf sf-no-children" id="menu-43146-1">
#             <a class="sf-depth-2" href="/resource/professional-development-teachers">
#              Professional Development Kits for Teacher Training
#             </a>
#            </li>
#            <li class="middle even sf-item-4 sf-depth-2 leaf sf-no-children" id="menu-43151-1">
#             <a class="sf-depth-2" href="/resource/professional-development-principals">
#              Professional Development Kits for Principal Training
#             </a>
#            </li>
#            <li class="middle odd sf-item-5 sf-depth-2 leaf sf-no-children" id="menu-43191-1">
#             <a class="sf-depth-2" href="/resource/training-calendar-for-network-teams">
#              Training Calendar for Network Teams
#             </a>
#            </li>
#            <li class="middle even sf-item-6 sf-depth-2 leaf sf-total-children-1 sf-parent-children-0 sf-single-children-1 menuparent" id="menu-43196-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              2015 Network Team Institutes
#             </a>
#             <ul>
#              <li class="firstandlast odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43321-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-march-17-20-2015">
#                Network Team Institute: March 17-20 2015
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="middle odd sf-item-7 sf-depth-2 leaf sf-total-children-6 sf-parent-children-0 sf-single-children-6 menuparent" id="menu-43161-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              2014 Network Team Institutes
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43201-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-february-4-7-2014">
#                Network Team Institute: February 4-7, 2014
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43206-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-may-13-16-2014">
#                Network Team Institute: May 13-16, 2014
#               </a>
#              </li>
#              <li class="middle odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43211-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-july-7-11-2014">
#                Network Team Institute: July 7-11, 2014
#               </a>
#              </li>
#              <li class="middle even sf-item-4 sf-depth-3 leaf sf-no-children" id="menu-43216-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-august-5-8-2014">
#                Network Team Institute: August 5-8, 2014
#               </a>
#              </li>
#              <li class="middle odd sf-item-5 sf-depth-3 leaf sf-no-children" id="menu-43221-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-october-7-10-2014">
#                Network Team Institute: October 7-10, 2014
#               </a>
#              </li>
#              <li class="last even sf-item-6 sf-depth-3 leaf sf-no-children" id="menu-43226-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-december-9-12-2014">
#                Network Team Institute: December 9-12, 2014
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="middle even sf-item-8 sf-depth-2 leaf sf-total-children-4 sf-parent-children-0 sf-single-children-4 menuparent" id="menu-43166-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              2013 Network Team Institutes
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43246-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-february-4-7-2013">
#                Network Team Institute: February 4-7, 2013
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43241-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-may-13-16-2013">
#                Network Team Institute: May 13-16, 2013
#               </a>
#              </li>
#              <li class="middle odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43236-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-july-8-12-2013">
#                Network Team Institute: July 8-12, 2013
#               </a>
#              </li>
#              <li class="last even sf-item-4 sf-depth-3 leaf sf-no-children" id="menu-43231-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-november-12-15-2013">
#                Network Team Institute: November 12-15, 2013
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="middle odd sf-item-9 sf-depth-2 leaf sf-total-children-11 sf-parent-children-0 sf-single-children-11 menuparent" id="menu-43171-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              2012 Network Team Institutes
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43296-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-january-17-19-2012">
#                Network Team Institute: January 17-19, 2012
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43291-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-february-8-10-2012">
#                Network Team Institute: February 8-10, 2012
#               </a>
#              </li>
#              <li class="middle odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43286-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-march-12-14-2012">
#                Network Team Institute: March 12-14, 2012
#               </a>
#              </li>
#              <li class="middle even sf-item-4 sf-depth-3 leaf sf-no-children" id="menu-43281-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-april-16-18-2012">
#                Network Team Institute: April 16-18, 2012
#               </a>
#              </li>
#              <li class="middle odd sf-item-5 sf-depth-3 leaf sf-no-children" id="menu-43276-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-may-14-17-2012">
#                Network Team Institute: May 14-17, 2012
#               </a>
#              </li>
#              <li class="middle even sf-item-6 sf-depth-3 leaf sf-no-children" id="menu-43271-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-june-5-7-2012">
#                Network Team Institute: June 5-7, 2012
#               </a>
#              </li>
#              <li class="middle odd sf-item-7 sf-depth-3 leaf sf-no-children" id="menu-43301-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-july-9-13-2012">
#                Network Team Institute: July 9-13, 2012
#               </a>
#              </li>
#              <li class="middle even sf-item-8 sf-depth-3 leaf sf-no-children" id="menu-43266-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-august-13-17-2012">
#                Network Team Institute: August 13-17, 2012
#               </a>
#              </li>
#              <li class="middle odd sf-item-9 sf-depth-3 leaf sf-no-children" id="menu-43261-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-september-12-13-2012">
#                Network Team Institute: September 12-13, 2012
#               </a>
#              </li>
#              <li class="middle even sf-item-10 sf-depth-3 leaf sf-no-children" id="menu-43256-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-october-10-11-2012">
#                Network Team Institute: October 10-11, 2012
#               </a>
#              </li>
#              <li class="last odd sf-item-11 sf-depth-3 leaf sf-no-children" id="menu-43251-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-november-26-29-2012">
#                Network Team Institute: November 26-29, 2012
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="last even sf-item-10 sf-depth-2 leaf sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent" id="menu-43176-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              2011 Network Team Institutes
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43316-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-august-1-5-2011">
#                Network Team Institute: August 1-5, 2011
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43306-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-november-29-30-2011">
#                Network Team Institute: November 29-30, 2011
#               </a>
#              </li>
#              <li class="last odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43311-1">
#               <a class="sf-depth-3" href="/resource/network-team-institute-materials-november-2-3-2011">
#                Network Team Institute: November 2-3, 2011
#               </a>
#              </li>
#             </ul>
#            </li>
#           </ul>
#          </li>
#          <li class="last even sf-item-6 sf-depth-1 leaf sf-total-children-3 sf-parent-children-2 sf-single-children-1 menuparent" id="menu-43121-1">
#           <a class="sf-depth-1 menuparent" href="/parent-family-library">
#            Parents and Families
#           </a>
#           <ul>
#            <li class="first odd sf-item-1 sf-depth-2 leaf sf-no-children" id="menu-43346-1">
#             <a class="sf-depth-2" href="/parent-family-library">
#              Parent and Family Library
#             </a>
#            </li>
#            <li class="middle even sf-item-2 sf-depth-2 leaf sf-total-children-3 sf-parent-children-0 sf-single-children-3 menuparent" id="menu-43336-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              Resources for Parents &amp; Families
#             </a>
#             <ul>
#              <li class="first odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43351-1">
#               <a class="sf-depth-3" href="/parent-guides-to-the-common-core-standards">
#                Guides to the Common Core Standards
#               </a>
#              </li>
#              <li class="middle even sf-item-2 sf-depth-3 leaf sf-no-children" id="menu-43356-1">
#               <a class="sf-depth-3" href="/educational-activities-for-parents-and-students">
#                Educational Activities
#               </a>
#              </li>
#              <li class="last odd sf-item-3 sf-depth-3 leaf sf-no-children" id="menu-43361-1">
#               <a class="sf-depth-3" href="/videos-for-parents">
#                Videos
#               </a>
#              </li>
#             </ul>
#            </li>
#            <li class="last odd sf-item-3 sf-depth-2 leaf sf-total-children-1 sf-parent-children-0 sf-single-children-1 menuparent" id="menu-43341-1">
#             <a class="sf-depth-2 menuparent nolink" tabindex="0">
#              Resources for Educators
#             </a>
#             <ul>
#              <li class="firstandlast odd sf-item-1 sf-depth-3 leaf sf-no-children" id="menu-43366-1">
#               <a class="sf-depth-3" href="/resource/planning-a-parent-workshop-toolkit-for-parent-engagement">
#                Planning a Parent Workshop: Toolkit for Parent Engagement
#               </a>
#              </li>
#             </ul>
#            </li>
#           </ul>
#          </li>
#         </ul>
#        </nav>
#       </section>
#      </div>
#     </div>
#    </div>
#   </header>
#   <div class="main-container container">
#    <header id="page-header" role="banner">
#    </header>
#    <!-- /#page-header -->
#    <div class="row">
#     <div class="col-md-12">
#      <section class="col-sm-12">
#       <div class="row">
#        <div class="col-md-8">
#         <ul class="breadcrumb">
#          <li>
#           <a class="section home" href="/" title="EngageNY.org">
#            <i aria-hidden="true" class="icon-eny-dashboard">
#            </i>
#            <span class="sr-only">
#             Home
#            </span>
#           </a>
#          </li>
#          <li>
#           <a class="section video" href="/video-library" title="Video Library">
#            Video Library
#           </a>
#          </li>
#          <li>
#           <a class="active" href="/content/nysut-rubric-teacher-selects-appropriate-curricular-materials-and-resources">
#            NYSUT Rubric: Teacher Selects Appropriate Curricular Materials and Resources
#           </a>
#          </li>
#         </ul>
#        </div>
#        <div class="col-md-4">
#         <div class="pull-right">
#         </div>
#         <div class="page-links">
#          <a class="print-page btn btn-sm btn-info print-hidden" href="javascript:window.print()" rel="nofollow" title="Print this page">
#           <i class="fa fa-print fa-spaced">
#           </i>
#           Print
#          </a>
#         </div>
#        </div>
#       </div>
#       <div class="row">
#        <div class="col-md-12">
#        </div>
#       </div>
#       <a id="main-content">
#       </a>
#       <div class="region region-content">
#        <section class="block block-system clearfix" id="block-system-main">
#         <div class="bootstrap-twocol-stacked" id="video-utility">
#          <div class="row">
#           <div class="panel-panel top col-xs-12 col-sm-12 col-md-12 col-lg-12">
#            <div class="row">
#             <div class="col-md-12">
#              <div class="panel-pane pane-video-album pane-thin-padding">
#               <div class="pane-content book-navigation clearfix">
#                <a class="book-map-link" href="/content/nysut-rubric-teacher-selects-appropriate-curricular-materials-and-resources" title="NYSUT Rubric: Teacher Selects Appropriate Curricular Materials and Resources">
#                 <h1 class="book-title" style="text-align: center;">
#                  NYSUT Rubric: Teacher Selects Appropriate Curricular Materials and Resources
#                 </h1>
#                </a>
#                <div class="row">
#                 <div class="col-xs-12 col-md-4 col-md-push-4">
#                  <strong class="book-page-title">
#                   Video
#                   <span id="current">
#                    1
#                   </span>
#                   of
#                   <span id="count">
#                    2
#                   </span>
#                  </strong>
#                 </div>
#                 <div class="col-xs-6 col-md-4 col-md-pull-4 book-nav-prev">
#                  <a class="btn btn-sm btn-primary print-hidden" href="#prev" title="Go to Previous Video">
#                   <span class="inner">
#                    <span class="text">
#                     <i aria-hidden="true" class="fa fa-angle-left">
#                     </i>
#                     <strong>
#                      Prev
#                     </strong>
#                     <em class="title visible-md-inline visible-lg-inline">
#                     </em>
#                    </span>
#                   </span>
#                  </a>
#                 </div>
#                 <div class="col-xs-6 col-md-4 book-nav-next">
#                  <a class="btn btn-sm btn-primary print-hidden" href="#next" title="Go to Next Video">
#                   <span class="inner">
#                    <span class="text">
#                     <strong>
#                      Next
#                     </strong>
#                     <em class="title visible-md-inline visible-lg-inline">
#                     </em>
#                     <i aria-hidden="true" class="fa fa-angle-right">
#                     </i>
#                    </span>
#                   </span>
#                  </a>
#                 </div>
#                </div>
#               </div>
#              </div>
#             </div>
#            </div>
#            <div class="row" id="video-album">
#             <div class="col-md-8">
#              <div class="panel-pane pane-video-album pane-thumbnails">
#               <div class="pane-content album-videos-wrapper">
#                <ul id="album-videos">
#                 <li>
#                  <div class="field-name-field-video">
#                   <div class="media-vimeo-video media-vimeo-1">
#                    <iframe allowfullscreen="" class="media-vimeo-player" frameborder="0" height="334" id="media-vimeo-148668400" src="//player.vimeo.com/video/148668400?api=1&amp;player_id=media-vimeo-148668400&amp;color=" title="Teacher selects appropriate curricular materials and resources - Example 1" width="592">
#                     Video of Teacher selects appropriate curricular materials and resources - Example 1
#                    </iframe>
#                   </div>
#                   <div class="media-youtube-video media-youtube-1">
#                    <iframe allowfullscreen="" class="media-youtube-player" frameborder="0" height="334" id="media-youtube-l8ss7j-j5ys" name="Teacher selects appropriate curricular materials and resources - Example 1" src="https://www.youtube.com/embed/l8sS7j-j5ys?wmode=opaque&amp;controls=&amp;enablejsapi=1&amp;playerapiid=media-youtube-l8ss7j-j5ys" title="Teacher selects appropriate curricular materials and resources - Example 1" width="592">
#                     Video of Teacher selects appropriate curricular materials and resources - Example 1
#                    </iframe>
#                   </div>
#                  </div>
#                  <h3>
#                   Teacher Selects Appropriate Curricular Materials and Resources - Example 1
#                  </h3>
#                  <a class="video-album-watch btn btn-large" href="/resource/teacher-selects-appropriate-curricular-materials-and-resources-example-1" title="Teacher Selects Appropriate Curricular Materials and Resources - Example 1">
#                   More about this video
#                  </a>
#                 </li>
#                 <li>
#                  <div class="field-name-field-video">
#                   <div class="media-vimeo-video media-vimeo-2">
#                    <iframe allowfullscreen="" class="media-vimeo-player" frameborder="0" height="334" id="media-vimeo-148669140" src="//player.vimeo.com/video/148669140?api=1&amp;player_id=media-vimeo-148669140&amp;color=" title="Teacher selects appropriate curricular materials and resources - Example 2" width="592">
#                     Video of Teacher selects appropriate curricular materials and resources - Example 2
#                    </iframe>
#                   </div>
#                   <div class="media-youtube-video media-youtube-2">
#                    <iframe allowfullscreen="" class="media-youtube-player" frameborder="0" height="334" id="media-youtube-v-fdg4sy614" name="Teacher selects appropriate curricular materials and resources - Example 2" src="https://www.youtube.com/embed/V_FdG4sy614?wmode=opaque&amp;controls=&amp;enablejsapi=1&amp;playerapiid=media-youtube-v-fdg4sy614" title="Teacher selects appropriate curricular materials and resources - Example 2" width="592">
#                     Video of Teacher selects appropriate curricular materials and resources - Example 2
#                    </iframe>
#                   </div>
#                  </div>
#                  <h3>
#                   Teacher Selects Appropriate Curricular Materials and Resources - Example 2
#                  </h3>
#                  <a class="video-album-watch btn btn-large" href="/resource/teacher-selects-appropriate-curricular-materials-and-resources-example-2" title="Teacher Selects Appropriate Curricular Materials and Resources - Example 2">
#                   More about this video
#                  </a>
#                 </li>
#                </ul>
#                <br/>
#                <div class="video-album-body">
#                 <p>
#                  These videos of exemplary teacher practice are aligned to:
#                 </p>
#                 <p>
#                  <strong>
#                   <a href="http://usny.nysed.gov/rttt/teachers-leaders/practicerubrics/Docs/nysut-rubric-2014.pdf">
#                    NYSUT’s Teacher Practice Rubric
#                   </a>
#                  </strong>
#                 </p>
#                 <ul>
#                  <li>
#                   Standard II: Knowledge of Content and Instructional Planning
#                   <ul>
#                    <li>
#                     Element II.6: Teachers evaluate and utilize curricular materials and other appropriate resources to promote student success in meeting learning goals.
#                     <ul>
#                      <li>
#                       Element II.6.B: Selects Materials and Resources
#                      </li>
#                     </ul>
#                    </li>
#                   </ul>
#                  </li>
#                 </ul>
#                </div>
#               </div>
#               <div class="pane-footer">
#                <div class="row">
#                 <div class="col-sm-12">
#                  <div class="share-bar print-hidden">
#                   <div class="row">
#                    <div class="col-sm-5">
#                     <div class="share-icons addthis_sharing_toolbox">
#                     </div>
#                    </div>
#                    <div class="col-sm-7" style="text-align: right;">
#                     <ul class="list-inline action-buttons">
#                      <li class="add-to-discussion">
#                      </li>
#                      <li>
#                      </li>
#                      <li class="this-like">
#                       <span class="">
#                        <div class="rate-widget-1 rate-widget clear-block rate-average rate-widget-nysed_like rate-cd6d62eb655ef3de80d81a1773ba2b9f rate-node-40756-1-1--2" id="rate-node-40756-1-1--2">
#                         <a class="rate-button btn btn-xs btn-info" href="/content/nysut-rubric-teacher-selects-appropriate-curricular-materials-and-resources?rate=UJGsnBB3drqCg0mMif3zgNL67074eEozrwIdBae_gCI" rel="nofollow">
#                          <i class="fa fa-thumbs-up fa-spaced">
#                          </i>
#                          Like
#                          <span class="count">
#                           (107)
#                          </span>
#                         </a>
#                        </div>
#                       </span>
#                      </li>
#                     </ul>
#                    </div>
#                   </div>
#                  </div>
#                 </div>
#                </div>
#               </div>
#              </div>
#             </div>
#             <div class="col-md-4">
#              <div class="panel-pane pane-video-album pane-organized-list pane-thumbnails hidden-sm hidden-xs">
#               <div class="pane-content album-teasers-wrapper clearfix">
#                <ul id="album-teasers">
#                 <li class="clearfix slick-teasers">
#                  <a data-slide-index="0" href="#">
#                   <img alt="Teacher selects appropriate curricular materials and resources - Example 1" class="img-responsive" height="94" src="https://www.engageny.org/sites/default/files/styles/video-album-image/public/media-youtube/l8sS7j-j5ys.jpg?itok=rOfs624v" title="" width="94"/>
#                   <span class="teaser-title">
#                    Teacher Selects Appropriate Curricular Materials and Resources - Example 1
#                   </span>
#                  </a>
#                 </li>
#                 <li class="clearfix slick-teasers">
#                  <a data-slide-index="1" href="#">
#                   <img alt="Teacher selects appropriate curricular materials and resources - Example 2" class="img-responsive" height="94" src="https://www.engageny.org/sites/default/files/styles/video-album-image/public/media-youtube/V_FdG4sy614.jpg?itok=ZS8yZNOb" title="" width="94"/>
#                   <span class="teaser-title">
#                    Teacher Selects Appropriate Curricular Materials and Resources - Example 2
#                   </span>
#                  </a>
#                 </li>
#                </ul>
#               </div>
#              </div>
#             </div>
#            </div>
#           </div>
#          </div>
#          <div class="row">
#           <div class="panel-panel left col-md-8">
#            <div class="panel-pane pane-views pane-meta-data-dl panel-pane pane-all-tags panel-pane pane-secondary">
#             <h2 class="pane-title">
#              <i aria-hidden="true" class="fa fa-cubes">
#              </i>
#              Tags
#             </h2>
#             <div class="pane-content">
#              <div class="view view-meta-data-dl view-id-meta_data_dl view-display-id-block_1 view-dom-id-365415d04d3260d3219d5fe73a4621b6">
#               <div class="view-content">
#                <div class="metatag-dl clearfix">
#                 <dl class="metatag-dl clearfix">
#                  <dt>
#                   Created On:
#                  </dt>
#                  <dd>
#                   Wed 01/20/2016  -
#                  </dd>
#                  <dt class="meta-posted">
#                   Posted By
#                  </dt>
#                  <dd class="meta-posted">
#                   NYSED
#                  </dd>
#                  <dt>
#                   Topic(s):
#                  </dt>
#                  <dd>
#                   <a href="/topic/teacherleader-effectiveness-0">
#                    Teacher/Leader Effectiveness
#                   </a>
#                  </dd>
#                  <dt>
#                   End User:
#                  </dt>
#                  <dd>
#                   <a href="/end-user/teacher">
#                    Teacher
#                   </a>
#                  </dd>
#                  <dt>
#                   Media Type:
#                  </dt>
#                  <dd>
#                   <a href="/media-type/video">
#                    Video
#                   </a>
#                  </dd>
#                  <dt>
#                   Resource Type:
#                  </dt>
#                  <dd>
#                   <a href="/resource-type/video-albums">
#                    Video Albums
#                   </a>
#                  </dd>
#                  <dt>
#                   Creative Commons License:
#                  </dt>
#                  <dd class="meta-cc-image">
#                   <a class="cc-small" href="//creativecommons.org/licences/by-nc-sa/3.0/us" target="_blank">
#                    <img alt="Creative Commons Licence" height="15px" src="//i.creativecommons.org/l/by-nc-sa/3.0/us/80x15.png" title="" width="80px"/>
#                   </a>
#                  </dd>
#                 </dl>
#                </div>
#               </div>
#              </div>
#             </div>
#            </div>
#           </div>
#          </div>
#         </div>
#        </section>
#       </div>
#      </section>
#     </div>
#    </div>
#   </div>
#   <footer class="footer">
#    <div class="container print-hidden" id="footer">
#     <div class="container footer-row col-xs-12">
#      <div class="footer-left">
#       <p class="footer-address">
#        <a href="http://www.nysed.gov/" rel="noopener noreferrer" target="_blank">
#         <img alt="EngageNY is a NYSED website that provides resources for educators and parents." src="/sites/all/themes/eny_subtheme/img/nysedlogo_wht.png"/>
#        </a>
#       </p>
#       <p class="footer-address">
#        Engage NY
#       </p>
#       <p class="footer-address">
#        New York State Education Department
#       </p>
#       <p class="footer-address">
#        89 Washington Avenue
#       </p>
#       <p class="footer-address">
#        Albany, New York 12234
#       </p>
#       <p class="footer-address">
#        <a href="mailto:engagenysupport@nysed.gov?Subject=EngageNY" target="_top">
#         engagenysupport@nysed.gov
#        </a>
#       </p>
#      </div>
#      <div class="footer-right">
#       <div class="social-media">
#        <a href="http://twitter.com/EngageNY" rel="noopener noreferrer" target="_blank" title="Visit EngageNY on Twitter">
#         <span class="fa-stack fa-lg">
#          <span class="sr-only">
#           Visit EngageNY on Twitter
#          </span>
#          <i aria-hidden="true" class="fa fa-square fa-stack-2x">
#          </i>
#          <i aria-hidden="true" class="fa fa-twitter-square fa-stack-2x fa-top">
#          </i>
#         </span>
#        </a>
#        <a href="http://www.facebook.com/EngageNY" rel="noopener noreferrer" target="_blank" title="Visit EngageNY on Facebook">
#         <span class="fa-stack fa-lg">
#          <span class="sr-only">
#           Visit EngageNY on Facebook
#          </span>
#          <i aria-hidden="true" class="fa fa-square fa-stack-2x">
#          </i>
#          <i aria-hidden="true" class="fa fa-facebook-square fa-stack-2x fa-top">
#          </i>
#         </span>
#        </a>
#        <a href="http://vimeo.com/user7931682" rel="noopener noreferrer" target="_blank" title="Visit EngageNY on Vimeo">
#         <span class="fa-stack fa-lg">
#          <span class="sr-only">
#           Visit EngageNY on Vimeo
#          </span>
#          <i aria-hidden="true" class="fa fa-square fa-stack-2x">
#          </i>
#          <i aria-hidden="true" class="fa fa-vimeo-square fa-stack-2x fa-top">
#          </i>
#         </span>
#        </a>
#        <a href="/rss" title="Subscribe via RSS">
#         <span class="fa-stack fa-lg">
#          <span class="sr-only">
#           Subscribe via RSS
#          </span>
#          <i aria-hidden="true" class="fa fa-square fa-stack-2x">
#          </i>
#          <i aria-hidden="true" class="fa fa-rss-square fa-stack-2x fa-top">
#          </i>
#         </span>
#         <span class="sr-only sr-only-focusable">
#          Subscribe via RSS
#         </span>
#        </a>
#       </div>
#       <div class="search-form">
#        <form action="/search-site/" id="footer-search" method="get" name="search_form">
#         <label class="sr-only sr-only-focusable" for="query">
#          Search
#         </label>
#         <input class="field_search" id="query" name="search" placeholder="Search" size="30" title="search" type="text" value=""/>
#        </form>
#       </div>
#       <div id="terms-of-use">
#        <p>
#         <a href="/terms-of-use" title="Terms of Use">
#          EngageNY Terms of Use
#         </a>
#         |
#         <a class="ext" href="http://www.nysed.gov/terms-of-use#Accessibility" rel="noopener noreferrer" target="_blank" title="Accessibility">
#          Accessibility
#          <span class="ext">
#           <span class="element-invisible">
#            (link is external)
#           </span>
#          </span>
#         </a>
#        </p>
#       </div>
#      </div>
#     </div>
#    </div>
#   </footer>
#   <script src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-556caa5d37346a5e" type="text/javascript">
#   </script>
#   <script src="/sites/default/files/advagg_js/js__i11V-7AETPhfL9YzRpXBpECwVkYyQ_ahu2eHxES_mK0__S79mhsO6q7fWONLNt9XSEZx-JmiQeAEtuPkuVxIEjpY__ENQm_6H-iTBcm2G6yrSzwAbhe4gKYe46HYukHKmJLOo.js" type="text/javascript">
#   </script>
#  </body>
# </html>