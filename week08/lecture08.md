---
title: Lecture 8
layout: lecture
include_vega: true
visible_lec: true
visible_n: true
---

<!-- .slide: class="titleslide" -->

# Data Visualization
<div style="height: 6.0em;"></div>
## Jill P. Naiman
## Spring 2019 (Online)
## Lecture 8

---

## Quick announcements

Unless it is absolutely impossible, please post your questions in the Slack channel first.

This will help keep me from having to repeat answers in emails and get you help more quickly.

Sharing is caring! :)

---

## Quick announcements

Limited internet availability March 15-24.

---

## Quick announcements

Homework grades coming!

---

## Warm-Up to the Warm-Up activity

 * https://zzzev.com/movies

---

## Warm-Up Activity

 1. What is the visualization trying to show?
 1. What are its methods?
 1. What are the strengths / weaknesses?


 (Image on following slide is from https://wapo.st/2HVLqUw)

---

<!-- .slide: data-background-image="https://pbs.twimg.com/media/DY5aB0MVQAIoCPY.jpg" data-background-size="auto 90%" -->

---

## Today

 * Evaluating Visualization Systems
 * Markdown (leading up to Idyll next week)
 * Maps
   * Projections
   * Coordinate Systems
   * Plotting with CartoPy

---

</br>
</br>
</br>
# Topic 1: Evaluating Visualization Engines

---

## Evaluating Visualization Engines

 * Costs
 * Functionality
 * Aesthetics

notes: is this engine free or do you have to pay for it?  Does it do what I want?
Does its plots look like plots I want to make?

---

## Choices

 * Can I get ahold of this software?
 * Do I install it, or do I use it on a server?
 * What's the user interface like?
 * Is it declarative or is it imperative (procedural)?

---

## License: Software

 * What can you do with the software?
 * Can you study the software?
 * Who can you share it with?
 * Who can you give your visualization derivative works to?

---

## License: Software

 * Copyleft: share and share-alike
 * Non-copyleft: share, but don't necessarily need to share-alike
 * https://choosealicense.com/

notes: this website has a bunch of "auto" generated licences, depending on what kind of license
you want *your* software to use

If you are ever in a position to create software, you can check this out to see what sorts of options you have.

Also, many of the open source packages we'll be using (including python) use a specific kind of license.  A lot of folks use the MIT licenses, fyi.

---

## License: Data

 * What can you do with the data?
 * How do you credit that data?
 * Can the data be redistributed, remixed, modified?
 * http://opendefinition.org/guide/data/
 * https://theodi.org/guides/publishers-guide-open-data-licensing

notes: additionally, the data might have a specific license.  So maybe you can use the data for your viz, but not share the data itself with others.

How can the data be modified?  Can you share the modified data?

---

## Accessibility

 * Is the software installed locally on your machine?
 * Is it hosted at a local or remote instance?
 * Who owns the visualizations, and how is access to them controlled?

---

## Interface

How do you interact with the software?

 * Declarative: how do you want the plot to look?
 * Imperative/Procedural: what are the steps to make the plot look that way?

---

## Example Declarative

```python
Chart(df).mark_bar().encode(
    X('precipitation', bin=True),
    Y('count(*):Q')
)
```

(From [Altair Docs](https://altair-viz.github.io/tutorials/exploring-weather.html))

<!-- .slide: data-background-image="images/altair_example01.png" data-background-size="30% auto" data-background-position="right 20% bottom 20%" -->

---

## Evaluation: Costs

The "cost" of software is not exclusively the number of dollars you place on
the counter when you get a big cardboard box with marketing blurbs on the side.


---

## Evaluation: Costs

The "cost" of software is not exclusively the number of dollars you place on
the counter when you get a big cardboard box with marketing blurbs on the side.

Think about cost in several ways:

 * Monetary cost for *you* to use the software
 * Monetary cost for *someone else* to view your creations
 * Time cost of setting up the software/system
 * Cognitive cost for learning and using the system (documentation matters!)
 * Transmission cost for sharing your creations

---

## Evaluation: Aesthetics

Visualization is trendy.

When you construct something, think about the different ways it will be
interpreted:

---

## Evaluation: Aesthetics

Visualization is trendy.

When you construct something, think about the different ways it will be
interpreted:

 * How will the viewer understand the story of the data?
 * What will the _message_ of the visualization be?
 * Does the visualization say something about you and your handling of the data
   or utilization of tools?

---

</br>
</br>
</br>
# Topic 2: Markdown -> Idyll

---

## Markdown

We'll be using markdown a bit in this course, and even more so as we move
toward using Idyll.  You can think of it as standard text that we mark "up" to
provide indications of formatting:

 * To **bold**, use `**two asterisks**`
 * You can _italicize_ with `_underscores_`
 * Try out making bullet lists with `*` on each line
 * Links are fun: `[link text](http://example.com/)`

---

## Idyll

 * The editor: https://idyll-lang.org/editor
 * Examples: https://idyll-lang.org/gallery
   * a favorite: https://idyll-lang.org/gallery/the-d-i-y-data-of-fugazi
   * source code: https://github.com/mathisonian/diy-data-fugazi

---

## Idyll

 * The editor: https://idyll-lang.org/editor
 * Examples: https://idyll-lang.org/gallery
   * a favorite: https://idyll-lang.org/gallery/the-d-i-y-data-of-fugazi
   * source code: https://github.com/mathisonian/diy-data-fugazi

Install for next week/after spring break: https://idyll-lang.org/docs/getting-started

---

</br>
</br>
</br>
# Topic 3: Maps (& more on lying with data)

---

## Maps

Thinking about map projections is important for GIS data, and generic global info viz.

Let's start by thinking about the fact that...

---

## Maps

Thinking about map projections is important for GIS data, and generic global info viz.

Let's start by thinking about the fact that...

The Earth is a sphere.

(Fun question: to what degree is it a sphere?)

Have you ever wrapped a piece of paper around a ball?

---

## Projections

To map from one system to another, we must "project" from the original sphere
to the flat object we are observing.

What are some things we could preserve during such a projection?

<img src="images/mapwrap.gif" height="350"/>

notes:
One common conversion from sphere to plane is the squashed cylinder approach


---

## Projections

<img src="images/mapsplode.gif" height="350"/>

notes:
There's always a weird way to do it too. Here we're exploding the sphere into lots of 
mostly planar pieces that we can just lie out side-by-side.

---

## Projections: Common Preservations

Typically, one or more of these will be preserved, or at least, the distortion
will be minimized:

 * Area
 * Shape (Conformal)
 * Distance

---

## Projections: Common Preservations

Typically, one or more of these will be preserved, or at least, the distortion
will be minimized:

 * Area
 * Shape (Conformal)
 * Distance

There are other properties that can be preserved, as well.  Typically, maps
will be a "compromise" between preserving different properties.

What happens when we preserve one property over another?

---

Mercator is a "conformal" projection.  What is wrong with this?

<!-- .slide: data-background-image="images/mercator.png" data-background-size="auto 80%" -->

notes:
conformal = shape preserving (at the expense of accurate size)

---

## Projections: Distortions

We can characterize distortions in a projection by examining how a known shape
appears on them.  The Tissot Ellipse of Distortion is a method of showing this
by drawing circles of a fixed radius and examining their elliptical distortion.

<img src="images/Tissot_indicatrix_world_map_Mercator_proj.svg" height="400">

notes: so here for example, we see that the mercator projection has circles that
stay circles, though they change in relative size depending on where they are on the map

---

What do you notice?

<!-- .slide: data-background-image="images/mercator.png" data-background-size="auto 80%" -->

---

<!-- .slide: data-background-image="images/mercator_tissot.png" data-background-size="auto 80%" -->

notes:
Greenland and Antarctica are HUGE

---

<!-- .slide: data-background-image="images/transversemercator.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/transversemercator_tissot.png" data-background-size="auto 95%" -->

notes:
this projection is most accurate near the vertical center line

---

<!-- .slide: data-background-image="images/lambertcylindrical.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/lambertcylindrical_tissot.png" data-background-size="auto 95%" -->

notes:
Also known as "equirectangular", this is the favorite format of NASA because it's mathematically straightforward.

Note that the very top line of the image represents a single point on the globe.

---

<!-- .slide: data-background-image="images/mollweide.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/mollweide_tissot.png" data-background-size="auto 95%" -->

notes:
this is considered a good compromise between shape-preserving and angle preserving - but it's not perfect at either.

---

<!-- .slide: data-background-image="images/sinusoidal.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/sinusoidal_tissot.png" data-background-size="auto 95%" -->

notes:
this has even less distortion than mollweide, but the pointy ends don't feel very elegant and planet-like

---

<!-- .slide: data-background-image="images/gnomonic.png" data-background-size="auto 95%" -->

---

<!-- .slide: data-background-image="images/gnomonic_tissot.png" data-background-size="auto 95%" -->

notes:
this is another nightmare scenario like Mercator that was initially created for navigation. Straight lines on this map are the shortest route, but area, shape, and size are distorted.

---

## Discussion

What happens when we make a map that minimizes one region and maximizes
another?

---

## Discussion

<iframe width="1024" height="576" src="https://www.youtube.com/embed/vVX-PrBRtTY?rel=0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

notes:
after watching this, it's useful to know that the Peters projection is actually flawed as a teaching tool because of how much it distorts the shapes of countries near the poles.

---

## Discussion

[The True Size Of...](https://thetruesize.com)

notes:
Let's go see what Greenland actually looks like

---

## Discussion

Why is Europe at the center of all the maps we've looked at?

---

## Discussion

<img src="images/Azimuthal_equidistant_projection.jpg" width="512"/>

notes: there is nothing specifically wrong with putting a pole at the center of the map

---

## Discussion

<img src="images/Azimuthal_equidistant_tissot.png" width="512"/>

notes: also see here that now the equator is very distorted

---
## Discussion

<img src="images/Waterman_projection.png" width="512"/>

notes: or why bother having a spherical or rectangular shape at all?

---

## Discussion

<img src="images/Waterman_tissot.png" width="512"/>

notes: look how here there is very little distortion of size or shape

---

## Maps: Coordinate Systems

Once we have our system of transformation, we need to have a method of
representing positions.

Three common baseline methods:

 * Spherical coordinates
 * Latitude and Longitude
 * Degrees, minutes, seconds

Take care with:

 * Zero points
 * North/South, East/West
 * Ranges

---

## Intro to cartopy

CartoPy is a toolkit that builds on matplotlib to create fast, easy map
representations.

We will be relying on three key concepts:

 * Axes projections (similar to our polar projections)
 * Coordinate representations
 * Shapes

Using these, we will be able to build out many visualizations.

---

## CartoPy: Projections

We start out by constructing an axes in CartoPy that uses a given projection:

```python
import cartopy
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection=cartopy.crs.Mollweide())
ax.coastlines()
```

<!--What does this do?-->

---

## CartoPy: Coordinate Reference Systems

Transforming from a spherical reference system to a flat reference system is
the job of the projection; transforming from one discretization of a sphere to
another is the job of the coordinate system.

We can utilize Coordinate Reference Systems to describe the *input* coordinate
system and the *rasterization* system are described.

For example, there are several different ways to draw "straight" lines.  We can
do both `PlateCarree` and `Geodetic`.

```python
c_lat, c_lon = 40.1164, -88.2434
a_lat, a_lon = -18.8792, 47.5079
fig = plt.figure()
ax = fig.add_subplot(111, projection = cartopy.crs.PlateCarree())
ax.gridlines()
ax.coastlines()
ax.set_global()
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform = cartopy.crs.PlateCarree())
ax.plot([c_lon, a_lon], [c_lat, a_lat], transform = cartopy.crs.Geodetic())
```

---

<!-- .slide: data-background-image="images/map_plot1.png" data-background-size="auto 95%" -->

notes:
the blue line is Plate Carree, which maintains a straight line on the lat-lon grid

the orange line is Geodetic, which maintains a straight line around the curvature of the Earth

---

<!-- .slide: data-background-image="images/map_plot2.png" data-background-size="auto 95%" -->

notes:
now even the blue line has some curvature because we are picking a best-of-both-worlds Mollweide projection that doesn't perfectly preserve angle or area.

---

## Other Map Viz

 * Google Maps & Earth
 * WorldWide Telescope
 * CesiumJS
 * bqplot
 * Vega & friends

---

## <span style="font-size:22pt">Assignment 7: Evaluating Visualization Engines - Part 1</span>

<span style="font-size:18pt">Your assignment is to pick three of the following possibilities and write up a
set of comparisons for constructing the *same* visualization.</span>
 * <span style="font-size:14pt">Matplotlib</span>
 * <span style="font-size:14pt">Bokeh</span>
 * <span style="font-size:14pt">Plotly</span>
 * <span style="font-size:14pt">D3 / Vega / Vega-lite / Altair</span>
 * <span style="font-size:14pt">bqplot</span>
 * <span style="font-size:14pt">R / RStudio</span>

<span style="font-size:18pt">These comparisons should be:</span>
 * <span style="font-size:14pt">What is the license for the software?</span>
 * <span style="font-size:14pt">What is the focus of the software?</span>
 * <span style="font-size:14pt">Does it have interactivity, and how easy is it?</span>
 * <span style="font-size:14pt">What are the pros and cons of using it?</span>

---

## <span style="font-size:22pt">Assignment 7: Evaluating Visualization Engines - Part 2</span>

<span style="font-size:18pt">Install Idyll</span>

 * https://idyll-lang.org/editor