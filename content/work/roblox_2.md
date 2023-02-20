Title: Kia Ora Pīwakawaka
Date: 15/10/2022

The fantail/pīwakawaka is a friendly little bird known for following trampers around. As a part of the project I was working on, we had this goregous fantail asset that I had to figure out how to get to fly around, follow the player, and generally act like a fantail. 

![Alt]({static}/images/d/fantail_01.png){: .image-process-crisp}

**The problem:**

To get a duck believably acting like a duck, it only has to walk or swim. Most game platforms have some form of navmesh system combined with a pathfinding algorithm like A* to provide believable walking paths between points, while avoiding obstacles. While ducks, or other birds are on the ground, this can be used for good results.

Hawks and gulls, conversely, do spend a lot of time in the air. The simplest model just has them circling around a point. For variation, the point, circle radius, and the angle of the circle can all be varied to make the movement not feel repetitive. If more organic movement is required, they can be given a velocity, and an acceleration. A [steering force](https://www.kaspar.wtf/blog/steering-behaviors) is applied which pushes the bird towards a goal point. If the goal point changes position every so often, usually before the bird reaches it, you end up with a pretty good looking flight. Finally, a solution for obstacle avoidance is required, and something like [Sebastian Lague's](https://www.youtube.com/watch?v=bqtqltqcQhw) approach here works pretty well. 



However, like most small birds, the fantail doesn’t spend a lot of time just flying, or just walking. It tends to flit between branches, onto and around shrubbery. Its movement is  point to point and highly targeted. Therefore a different approach was needed.

**The Solution:**

The approach I settled on was to first manually place points the fantail could land on, shown underneath as grey spheres. While a system to find these points on any geometry would likely yield similar results over any size area I gave it, there wasn't time in this project to do so. If we come back to this part, and want the fantail to be able to travel much further, then an algorithmic approach would be preferable.

![Alt]({static}/images/d/fantail_02.png){: .image-process-crisp}

After that, an undirected graph could be constructed connecting all the points to other points within a set threshold. The fantail starts at one of these points, and is permitted to travel to any of the other points its current one is connected to. Add in an idle animation for when it’s sitting at a point, and a flying one for travel, and we have a pretty reasonable solution. 

Two issues remained however, the first was graph islands, and player following.

If two sections of points were far enough away from each other, then they would never get connected and the fantail could never leave that one little area. To combat this a second set of connections was constructed periodically with a distance threshold four times higher than the standard one. As each connection could only made once, this provided several links between islands, to ensure that there was at least one connection between them. 

Graph connections, normal in gray, long distance in orange:

![Alt]({static}/images/d/fantail_03.png){: .image-process-crisp}

Following the player was fortunately simple. When the fantail lands on a new point, and gets a new set of valid destinations, it also gets every point within a distance threshold from the player. Regardless of whether they are connected to the current point or not, these are always considered valid to travel to. The next destination point is taken from this combined list.

Here it is in action: 

<div style="padding:75% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/799655961?h=11a25c9a53&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen style="position:absolute;top:0;left:0;width:100%;height:100%;" title="FantailDemo.mp4"></iframe></div><script src="https://player.vimeo.com/api/player.js"></script>

**Further considerations:**

Weighting the decision between a point close to the player vs a normal node was tried, and found to be not necessary for the behaviour to work. 

The graph building is a fairly naive, running in n^2 time. While optimizations, like spacial segmentation were possible, simply running the algorithm once upon startup, and then passing references to nodes to all interested parties proved efficient enough. 

