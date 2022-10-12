<html>
<img src="Pyrate.svg" width="100%" height="100%">
<p class="has-line-data" data-line-start="0" data-line-end="1">A small, self-destructing Qt5 web browser written in python and designed for/with unique functions for Ubuntu.</p>
<h3 class="code-line" data-line-start=2 data-line-end=3 ><a id="What_do_you_mean_selfdestructing_2"></a>What do you mean self-destructing?</h3>
<blockquote>
<p class="has-line-data" data-line-start="3" data-line-end="4">When a Qt5 web browser is launched it creates a .local file that hosts all of the cookie-cache’s targeted by serverside cookies. I created a function titled “.abandonShip” that removes the QtWebBrowser folder entirely. I tested it against multiple serverside cookies and have yet to find one not removed by this process. That isnt to say it isnt possible, just that, for most practical purposes this proves effective.</p>
</blockquote>
<h3 class="code-line" data-line-start=5 data-line-end=6 ><a id="What_is_with_the_weirdLettering_5"></a>What is with the .weirdLettering()</h3>
<blockquote>
<p class="has-line-data" data-line-start="6" data-line-end="7">That is Qt5 syntax</p>
</blockquote>
<h3 class="code-line" data-line-start=8 data-line-end=9 ><a id="Ok_so_what_other_unique_functions_are_there_Its_just_a_browser_8"></a>Ok, so what other “unique” functions are there? It’s just a browser.</h3>
<blockquote>
<p class="has-line-data" data-line-start="9" data-line-end="10">True, there isnt anything new under the sun here (besides maybe the self-destruction thing.) It is .onion enabled so if you have already downloaded Tor you can now access .onion sites in .Pyrate aswell. It has the ability to play/load/view contents through drag and drop from your home folder making it useable beyond just visiting websites. It still has bookmarks, downloads, ect… However the way it is arranged is fairly unique:</p>
</blockquote>
<ol>
<li class="has-line-data" data-line-start="11" data-line-end="12">I did away with the over-packed menus of other browsers and consolidated the basic functionality into 3 comboboxes and a single url bar spread across 2 toolbars. This allows you to customize the layout, to an extent, without cluttering your view with dozens of buttons and menus.</li>
<li class="has-line-data" data-line-start="12" data-line-end="13">I never enabled redirects; I want full control of my boat in the digital ocean. You can still navigate to the redirect manually using the url bar but freedom and user control are central to the .Pyrate code.</li>
<li class="has-line-data" data-line-start="13" data-line-end="14">I never enabled direct downloads; Pyrates pick their cargo- if not you are just a privateer. You can download anything you want with .Pyrate, you just have to copy/paste or drag/drop the link into the url bar and select ‘.downLoad.’ under ‘.capsQuarters’- your options menu.</li>
<li class="has-line-data" data-line-start="14" data-line-end="15">I made an option to generate a qr of whatever is in the url bar: url, hashes, any text from your clipboard or that you drag/dropped from a page. It is the quickest way to share information from your lap/desktop to phone without signing/setting up or logging into anyting.</li>
<li class="has-line-data" data-line-start="15" data-line-end="16">All bookmarks are handled through saving HTML to local files. The idea was to create a form of script injection so basic and easy to access that anyone with a basic understanding of the concept and no knowledge of front end development could extract, read, copy/cut/paste and test their code all in a simple .txt format. I am fully aware that QT has an entire module for scripting- I aimed more for K.I.S.S. with the context of education in mind. If you want to add script injection features, I will leave a link to the Qt page for scripting in python and you can add it yourself or, if you would like to add to/fork this project feel free.</li>
<li class="has-line-data" data-line-start="16" data-line-end="17">I made an option called “.djanGo()” that automates the setup of a new django web-framework project with the help of a dialogue box. Nobody <strong><em>NEEDS</em></strong> this, you should be able to handle that on your own if youre messing with django. My only reasoning is to “automate the boring stuff.” Not to mention, you can self host your bookmarks, if you were so inclined.</li>
<li class="has-line-data" data-line-start="17" data-line-end="18">This browser is not designed for the basic user: it was written on Ubuntu FOSS with FOSS at the root of the idea. It likely wont port well to other platforms without tweaking a few things but it shouldnt be a massive process to correct.</li>
<li class="has-line-data" data-line-start="18" data-line-end="19">‘seaShanties’ is a <strong><em>demonstration</em></strong> for <strong><em>educational purposes only</em></strong> of the effectiveness of paring BeautifulSoup with a search engine for quickly gathering information on a topic aswell as a basic implimentation of data transfer from one program to another using .txt (this is usually done though .csv files, but for the sake of beginner approachability I went with .txt), and the usefulness of dequing processes atexit. Also, it downloads music. (<strong><em>Im not responsible if you download unauthorized songs, check your album search lists for download authorization with youtube before saving, you can always cancel the download of any video by pressing ctrl+c in your terminal if it violates copywright restrictions</em></strong>)</li>
<li class="has-line-data" data-line-start="19" data-line-end="20">Your homescreen is a local html file by default so you can copy/paste your own html onto or in place of the .Pyrate_Player.html template to customize your homescreen in a way other browsers wont let you.</li>
<li class="has-line-data" data-line-start="20" data-line-end="22">‘.hashWords’ is a tool to generate hashes of web objects by copying urls, links, or strings into the url bar and hitting ‘.hashWords’. This is useful for quickly compairing long urls/links, or even entire bodies of text or code snippets against simular objects. (Note, hashes are salted by default in python, therefore results vary from one instance of .Pyrate to the next. Put simply: dont use ‘.hashWords’ do generate a password no matter how much it sounds like the implied function. I assume you have seahorse or keypass.)</li>
</ol>
<h3 class="code-line" data-line-start=22 data-line-end=23 ><a id="Why_22"></a>Why?</h3>
<blockquote>
<p class="has-line-data" data-line-start="23" data-line-end="25">Occams razor: the simplest solution is the most likely one. You dont need 34mb to make a connection to a .onion website and you dont need machine learning to remove a server side cookie. If you browsing data is stored in memory, and your memory is reset when the power turns off, you automatically reset your browsing data on open/close.<br>
No one expects you to delete firefox and use .Pyrate but if youre looking for a fun project to reverse engineer/beautify or give to your teenage relative with the clear instructions <strong><em>NOT</em></strong> to abuse downloads, this might be it.</p>
</blockquote>
<h3 class="code-line" data-line-start=26 data-line-end=27 ><a id="WTF_is_pip_quick_26"></a>WTF is pip_quick?</h3>
<blockquote>
<p class="has-line-data" data-line-start="27" data-line-end="28">Sometimes you dont want to build and install a script/package, you just want to run it quickly and put it back in storage/delete it. That is where pip_quick comes in. You can still run <a href="http://setup.py">setup.py</a> but if you are ok with installing the dependencies outside of the script path and and in your .local file. You can clone .Pyrate and run it immediatly from whereever you cloned it- pip_quick will subprocess all of the installs for you, including the Qt5 dependencies.</p>
</blockquote>
<h3 class="code-line" data-line-start=29 data-line-end=30 ><a id="Notes_29"></a>Notes:</h3>
<p class="has-line-data" data-line-start="30" data-line-end="31"><em>If you want access to .onion sites aswell you will need to install tor on your own.</em></p>
<pre><code class="has-line-data" data-line-start="33" data-line-end="35" class="language-BASH">sudo pacman -S tor -y || sudo apt install tor -y &amp;&amp; sudo systemctl <span class="hljs-built_in">enable</span> tor &amp;&amp; sudo systemctl start tor
</code></pre>
<h3 class="code-line" data-line-start=36 data-line-end=37 ><a id="To_use_the_djanGO_feature_you_must_run_36"></a>To use the ‘.djanGO’ feature you must run</h3>
<pre><code class="has-line-data" data-line-start="39" data-line-end="41" class="language-BASH">pip install django
</code></pre>
<p class="has-line-data" data-line-start="42" data-line-end="43">*** Work in progress, more features in beta ***</p>
</html>
