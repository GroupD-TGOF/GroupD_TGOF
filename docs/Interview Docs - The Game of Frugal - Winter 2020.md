SUBJECT:   Initial interview with Jim Jones’ Games creative genius Sean.
DATE:  Winter Term 2020
RE: is the ‘Requirements Engineer”.

RE:  Thanks for taking the time to meet with me this afternoon.

Sean: Oh, it’s my pleasure. Mr. Jones said we were to give you all the 
help you needed in getting this game worked out.

RE: Mr. Jones said that you had played a major role in coming up with the Frupal game concept, could you tell me a little bit about it?

Sean: Sure. Frupal is based on the idea that the hero of the game is 
looking for some magic jewels that are hidden somewhere on the island of Frupal.   During the game, the hero travels around the island having 
adventures until they come upon these magic jewels.

RE: Adventures? What kind of adventures?

Sean: Oh, different things. I don’t know if you’d really call them 
adventures - maybe event is a better name for them. 
But for instance, finding something that will give them more energy or more money.

RE: Money? Energy? Where do these come in?

Sean: Well, when the hero starts out, they have a certain amount of 
energy, and each time they move, they lose some of it. So they need some way to boost it, otherwise the game would be over quickly.

RE: And money?

Sean: Oh yeah. So in order to get more energy, they need to buy it.

RE: So the hero starts out with cash in the bank too?

Sean: Yep.

RE: So how much energy and money do they start out with?



Sean: Well, that can vary. See, each player should be able to set up the 
amount of energy and money they start out with before they play the game. 
And if the player wanted to, they could do this before every game.


RE: Can the player change how much energy the hero uses up when they 
travel too?


Sean: No. In the case of expending energy when moving, the 
hero always looses one unit of energy every time they take a step.


RE: Tell me more about taking steps.

Sean: So the hero can take a step to the West, East, North or South.


RE: How far is a step, and is it always just one step?

Sean: Well, we think of the game area as being divided up into squares identified by coordinates, where the southwest corner of the game area is 
(1,1), and the northeast corner is (x,x), depending on how the player sets it up. A step moves you from one of these squares in to an adjacent /square.


RE: And is it always just one step?

Sean: That's right - each move is always a single step to the West, East, 
North or South.

RE: So at each move, the hero can step one position to the West, East, 
North or South, and they expend one unit of energy, right?

Sean: You've got it. They expend one unit of energy if the terrain is 
firm and level. Of course if the terrain is a bog or a forest, they use 
up more.

RE: So they don't always use up just one unit of energy?


Sean: That's right. If it is a bog or a forest, they use up two units of 
energy. 
If it is a grassy meadow - I mean - firm and level, then they 
expend one unit of energy when they take a step.

RE: So any other sorts of things we need to keep in mind when the hero is 
moving around?

Sean: Water.

RE: Water?

Sean: Yeah. If the hero encounters water, like a river or lake, they 
can't continue on in that direction ... it blocks them.

RE: So what happens if they encounter water?

Sean: Their position doesn't change. They stay where they are, but every 
time they try to go through the water, they consume a unit of energy unless they buy a boat.

RE: A boat? How do they buy a boat?

Sean: The hero can buy a bunch of different items. They can buy a Power 
Bar to get more energy, or a boat that allows them to travel over water. 
If they travel over water by boat, it doesn't consume any energy, so the 
movement is "free." They can also buy tools that can help them get rid of 
obstacles they might encounter.

RE : Obstacles? Like what?

Sean: Well, Blackberry Bushes, Big rocks, or Trees across the path.

RE: Where do tools come in?


Sean: If you encounter these obstacles without any tools, you use up 
extra energy to remove them from your path by hand. But if
you have the appropriate tool, you can remove the obstacle while expending very little energy. 
So if you have a Weed Whacker, you can easily cut through 
Blackberry Bushes compared to having to cut the vines by hand. If you 
have a jack hammer, you can remove rocks and boulders in your path for a 
lot less energy than if you try to bust them up by hand. A chain saw can 
remove trees from your way easier than using your pocket knife to whittle 
the tree down by hand.

RE: How much energy do these tools save, and how much do you have to pay for them?

Sean: The player should be able to specify that in a pre-game 
configuration, like I mentioned earlier. In fact, the player should be 
able to define obstacles, their behavior, and associated tools in this 
configuration, rather than being stuck with built- in obstacles and tools.

RE: Is there anything else the hero can buy?

Sean: I almost forgot. They should be able to buy binoculars.

RE: Binoculars? How does that work?

Sean: Well, ordinarily, the user can see, and remember, all the 
coordinates immediately surrounding them. That is, they can see 
obstacles, items they can buy, the type of terrain and so forth. For 
example, if the hero is at coordinate (12,15), and coordinate (13,15) is 
water, they can see that so they won't accidently walk into it. But they 
can't see two over at coordinate (14,15). If they buy a pair of 
binoculars, they can see out to two coordinates in each direction. In 
either case, once they've seen a coordinate, they can't "forget" it, 
so while they are playing that information is available to them.


RE: And I suppose the cost of the binoculars is specified in that pre-game configuration, right?

Sean: That's right. It's a file the game consults when it is starting up 
to get all the configuration data needed to create a custom experience 
for a player.

RE: So how does this file come to be created?


Sean: Well, from the game's start screen, you should be able to go to an 
administrator’s screen. This is where you can personalize stuff for the 
current and future games.

RE: What kinds of stuff?

Sean: Well, like I was saying, you can add obstacles, tools to deal with 
obstacles, the amount of money and energy you start with and so forth.

RE:Wow, this is a lot. Is there anything else about the game I should 
know?


Sean:  Well, we expect this to be a command line interface.

RE: OK. That sounds fine. I think I've got some CS300 students who can do this.

Sean:  Great, just as long as they're cheap.

RE:  Oh yeah. They like cost nothing.
