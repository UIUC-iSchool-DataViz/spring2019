---
title: Lecture 11
layout: lecture
include_vega: true
---

<!-- .slide: class="titleslide" -->

# Data Visualization
<div style="height: 6.0em;"></div>
## AJ Christensen
## Spring 2019
## Lecture 11

---

## Warm-Up Activity

 1. What is the visualization trying to show?
 1. What are its methods?
 1. What are the strengths / weaknesses?

[Flaws of a Boeing 737 Max](https://www.nytimes.com/interactive/2019/03/29/business/boeing-737-max-8-flaws.html)

---

# April 22nd at NCSA

We will meet in 1005 on the ground floor.

The address is 1205 W Clark St, just north of the Siebel computer science building.

---

## Today

 * Validation
 * Publishing
 * More on Idyll

---

## Validation

How do you know your visualization is actually useful? Is it...

 * More comprehensive or contextual
 * More revealing or educational
 * More fun or pleasant to use
 * More efficient or fast

notes:
What do we even mean "more than"? More than what?

More than just looking at numbers?

More than a previous visualization?

More than the state of the art?

---

## Validation

Why is validating a visualization important?

 1. The design space is huge
 1. Most designs are ineffective
 1. User-focused design is often an afterthought
 1. The "quality" of a visualization is subjective

notes:
Can you all think of a user experience that drives you nuts in your daily life? A pointless button in your email? A door that opens the wrong way? A noisy piece of machinery?

---

## Validation

What can a visualization designer get wrong?

 * Misunderstand the needs of the domain expert or educator
 * Interpret the data incorrectly
 * Represent the data in a visually confusing way
 * The software is too laggy or difficult to use in a practical setting

notes:
Any other ideas?

---

## Methods of Validation

Before developing your visualization system:

 1. Observe and interview target users or audience members
 1. Justify interaction design plans against the academic literature and existing tools
 1. Do an analysis of the complexity of the system

---

## Methods of Validation

After developing your visualization prototype:

 1. Measure system performance
 1. Usability studies (formal and/or informal)
 1. Measure human time to complete a task, or number of user erros
 1. Do a field study - perhaps even collect user data with the system

notes:
You don't have to do all of these all the time, but depending on the project they might all be a good idea

Also, remember to respect user privacy when collecting user data. This is extremely sensitive.

---

## Methods of Validation:

After publishing your visualization:

 1. Observe adoption rates
 1. Solicit anecdotal user feedback

notes:
This is especially valuable if you expect to have to make more than one visualization in your life. Building intuition for what works and what doesn't is a large part of the career success of a visualization designer.

The Advanced Visualization Lab interacts with audiences through lab demos and conference talks regularly to collect this kind of feedback.

---

## Validation in Final Project

Your peers will ask you questions at the end of your presentation. Try to understand what is working for them and what is not. It will help hone your instincts.

---

## Publishing

Your stunning visualizations will do no one any good if they reside only on your laptop. How do you get them out there?

 * The Internet
 * In-Person Presentation
 * Popular Media
 * Physical Objects

---

## Publishing for the Web

 * Raw HTML, CSS, SVG, and JavaScript
 * Content Management Systems
 * Idyll
 * GitHub Pages
 * Social Media

---

## Raw HTML, CSS, SVG, and JavaScript

Pros:
 * Less of a learning curve
 * Lots of documentation

Cons:
 * No reproducibility
 * LOTS of code writing
 * Locked in time - no software updates

---

## Content Management Systems

There are dozens of these, for instance: 
 * Squarespace
 * Wordpress
 * Wix
 * Drupal

<img src="images/cms.png" width="800"/>

notes:
Squarespace seems to be the favorite of small businesses. Drupal is great for large businesses.

---

## Content Management Systems

Pros:
 * Pre-built templates that might be updated by the development community
 * Plugins with visualization tools
 * Content updates are done by GUI

Cons: 
 * Visualization tools not automatically built in
 * More effort because they're meant for whole websites
 * Code (especially for plugins) can become outdated and incompatible

---

## Idyll

Pros:
 * Visualization-ready, compatible with Vega-Lite, D3.js, and Flourish
 * Modern features and design

Cons:
 * Less common syntax (Markdown)
 * Not well-documented
 * No guarantee of long-term support in the future

<img src="images/idyll.png" width="200"/>

---

## GitHub Pages

Pros: 
 * Community driven (there's lots of support)
 * Free hosting

Cons:
 * Community driven (there can be bugs and surprises)
 * All websites are static

<img src="images/githubpages.jpeg" width="200"/>

---

## Social Media

How can visualization be distributed on social media?
 * Images can be shared everywhere
 * Embedded videos using YouTube, Vimeo, FB video, etc
 * [SketchFab](https://sketchfab.com) scenes can be shared on Reddit, Facebook, and Twitter

notes:
The internet is visual, and increasingly about video (or at least animated gif)

Sketchfab is a great service for viewing 3D content in a web browser.

---

## Social Media

Pros:
 * Huge audience
 * Easy to target the communities you're trying to communicate with

Cons:
 * Limited functionality, especially wrt interactivity
 * Visualizations have shorter expiration date
 * No quality control

---

## Sharing Visualizations in Live Presentation

 * Jupyter Notebook (cleaned up)
 * PDF (3D capability!)
 * Powerpoint (3D capability!)
 * Mobile App
 * Printed on paper (300dpi, serif fonts, line thickness)
 * Custom in-house software (e.g. Bloomberg Terminal)

<img src="images/bloomberg.jpg" width="300"/>

notes:
Some of these are a bit outdated, but sometimes corporate environments require you to speak the language management wants you to speak.

---

## Sharing Visualizations through Popular Media

 * Videos and films

<img src="images/prison.gif" width="800"/>

notes:
This approach usually relies on more stylized treatments called "motion graphics".

Often the film approach depends on working with someone who produces movies who is looking for content. But some people will produce their own content (especially in short documentary format) for internet release.

---

## Sharing Visualizations through Popular Media

 * Museum exhibits

<img src="images/museum.png" width="800"/>

notes:
You get much more control when working with experts in museums, and you get to see your visualization blown up to huge sizes.

You still need to make a visualization that even a very small child will understand though.

---

## Sharing Visualizations through Popular Media

 * App Stores

<img src="images/wwt.png" width="800"/>

notes:
This is how you can reach people through their phones and popular new media like virtual reality.

---

## Making Visualization

 * 3D printing 
 * Printed leggings
 * Blankets
 * Whatever you can think of 
    * Visit [Instructables.com](https://instructables.com) for ideas!

<img src="images/blanket.jpg" width="400"/>

---

## Technical Limitations

 * Memory
 * Screen Size
 * Interaction technique (mouse and keyboard vs touchscreen)
 * Disk space

---

## More Idyll...

---

## Final Project: Part 2

Due by class on April 15th, submitted via Moodle in a Jupyter notebook.

As a group you should submit:

Code:
 * Jupyter notebook with an interactive dashboard that helps an expert explore your dataset thoroughly. There should be 4 linked visualizations all exploring the same dataset and all visible at the same time. (3 linked visualizations for teams of 3.)
 * Do not delete any cells, just comment them out. Show your work.

---

## Final Project: Part 2 (cont)

As a group you should submit:

Prose:
 * One paragraph explaining how to use the dashboard you created, to help someone who is not an expert understand your dataset. 
 * A list of 5 (or more) contextual datasets you have identified, links to where they reside, and a sentence about why they might be useful in telling the final story.
 * A brief description of which group members completed which tasks. There should be an equal division of labor. Each group member will be graded based on how well they completed their tasks. If one group member clearly does less work, they may receive a grade deduction.

