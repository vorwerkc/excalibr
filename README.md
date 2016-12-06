<html>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><h1 align="center">                                               
Installation Guide
</h1></p>
<h2 align="center">                                               
Conda Environments
</h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>A download and install guide to conda can be found on <a href="http://conda.pydata.org/docs/download.html">http://conda.pydata.org/docs/download.html</a>, and a really good description of first steps with conda are described here: <a href="http://conda.pydata.org/docs/test-drive.html">http://conda.pydata.org/docs/test-drive.html</a></p>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>I highly recommend to download the conda version, which contains python 3.5. If you do so, you need to create a conda environment to execute <tt>exciting</tt> python 2 EXCITINGSCRIPTS commands in:</p>

<pre><code>conda create --name exciting python=2.7

</code></pre>
<p>Next, you have to install some basic packages in this environment:</p>

<pre><code>source activate exciting
conda install lxml numpy</code></pre>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Then, before running commands from the EXCITINGSCRIPTS, you have to activate the environment:</p>

<pre><code>source activate exciting</code></pre>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h2 align="center">                                               
Install excalibr from Github
</h2>
</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>To obtain excalibr, you first need a github (www.github.com) account. 
Then, you generate a new python 3.5 environment with conda:</p>

<pre><code>conda create --name pm_dev

</code></pre>
<p>Activate it and install pip:</p>

<pre><code>source activate pm_dev
conda install pip

</code></pre>
<p>You can then clone the code:</p>

<pre><code>git clone -b master https://github.com/vorwerkc/excalibr.git

</code></pre>
<p>Change into the directory and pip install it:</p>

<pre><code>cd ./excalibr
pip install -e .</code></pre>

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">

</div>
</div>
</div>
    </div>
  </div>
</body>
</html>
