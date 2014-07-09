fitgrd
======

.fitgrd is the lightweight &amp; sexy looking responsive grid for your next awesome website.

Find the working demo here: www.fitgrd.com
It works in all modern Browsers and IE7 - IE10.



## What it is
.Fitgrd is not a framework. It's a solid foundation to build up your own responsive website. 
It is designed for rapid prototyping, but also runs well in production environments. 
This grid system is perfect for advanced web designers who don't want to have their pages look like "bootstraped". 
Everything but the grid is up to you and gives you the ability to save a lot of dispensable code. 
Give it a try and you'll love it.

## What you will get
.Fitgrd is divided into twelve columns with percentual widths. 
Each column has two percent of margin on both sides. I'm not a friend of heavy usage of media queries. 
So i included just two for the size of 36.5em(phones) and 48em(tablets). 
Write smart code and you will not need more.

## Note
Fitgrd is a product of much coffee and sleepless nights. 
I have many good ideas for further development which
will make your life easier as developer or designer. 
I would be delighted if you flattr fitgrd!

<a href="http://flattr.com/thing/1355012/fitgrd-the-sexy-looking-responsive-css-grid" target="_blank"><img src="http://api.flattr.com/button/flattr-badge-large.png" alt="Flattr this" title="Flattr this" border="0" /></a>

## Basic Setup

To add this to your website, simply include `fitgrd.pack.css` into your document's `<head>`

In order to guarantee a perfect responsive grid, follow the specs like:

- container (could be `header`, `div`, `article`, `footer` etc. with your class name)
	- class center
		- class row
			- classes fg1 - fg12 as much as you want
			
			
## Example

````html
<header>
	<div class="center">
		<div class="row">
			<section class="fg2">
				your logo
			</section>
			<section class="fg10">
				page navigation would go here
			</section>
		</div>
	</div>
</header>

<article class="your-class-name">
	<div class="center">
		<div class="row">
			<section class="fg4"> lorem ipsum ... </section>
			<section class="fg4"> lorem ipsum ... </section>
			<section class="fg4"> lorem ipsum ... </section>		
		</div>
	</div>
</article>

<footer>
	<div class="center">
		<div class="row">
			<section class="fg6"> footer copyright </section>
			<section class="fg6"> footer navigation </section>
		</div>
	</div>
</footer>

````

## Issues

If you build a fitgrd page that also should run in IE7:<br/>
Do not use left or right padding on `.fg1` to `.fg12`, otherwise the grid will not work correctly.<br/>
The problem is, that IE7 does not support the box-model property. 

There are also hacks and workarounds out there. But i am not a big fan of that.

## Licence

The MIT License (MIT)
Copyright (c) 2013 Jan Müller

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), 
to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
