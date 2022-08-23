# Cross device burger JS menu

## Description

Multilevel burger menu opening on hover on desktop or button on mobile device using vanilla javaScript

## Examples 👁️

![screenshot](https://user-images.githubusercontent.com/91592743/136660430-721571c5-efd0-4bcf-b6ec-bfc2b34ab366.png)

https://user-images.githubusercontent.com/91592743/136660423-20f82add-4031-4467-9b47-6919e6d599aa.mp4

---

## Technologies used 🛠️

<h3 align="left"> &nbsp  &nbsp  &nbsp Programming languages</h3>

<a href="https://www.w3.org/html/" target="_blank"> <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5" height="30"/> </a>
<a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3" height="30"/> </a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E" alt="JavaScript" height="30"/> </a>

---

## Features 💡

⚡️ Device detection\
⚡️ Responsive\
⚡️ No needed separate links for opening sub menu\
⚡️ Open on hover or button click\
⚡️ Cross device

## How To Use 🔧

Add script and styles to your html file.

Example of html structure:

```html
<div class="header__menu menu">
	<div class="menu__icon">
		<span></span>
	</div>
	<nav data-sub_menu_auto_close="true" class="menu__body">
		<ul class="menu__list">
			<li>
				<a data-goto=".page__section_1" href="" class="menu__link">Section 1</a>
			</li>
			<li>
				<a data-goto=".page__section_3" href="" class="menu__link">Section 3</a>
			</li>
			<li>
				<a href="" class="menu__link">Page 1</a>
				<span class="menu__arrow"></span>
				<ul class="menu__sub-list">
					<li>
						<a href="" class="menu__sub-link">Section page 1</a>
					</li>
					<li>
						<a href="" class="menu__sub-link">Section page 2</a>
					</li>
				</ul>
			</li>
			<li>
				<a href="" class="menu__link">Page 2</a>
			</li>
		</ul>
	</nav>
</div>
```

---

## Acknowledgments 🎁

Thanks to
[Евгений Андриканич](https://fls.guru/) ,
[Vladilen Minin](https://www.youtube.com/c/VladilenMinin) ,
[CS50](https://cs50.harvard.edu/college/2021/fall/) ,
[Александр Лущенко](https://itgid.info/) ,
[Vadim Makeev](https://www.youtube.com/channel/UCaTfYudJUVA8cV_But8KZVQ) ,
[Safak](https://github.com/safak) ,
[Adrian Hajdin](https://www.completepathtojavascriptmastery.com/) ,
[Sumit Dey](https://www.youtube.com/c/BackbenchCoder)
for motivational and helpful content

---
