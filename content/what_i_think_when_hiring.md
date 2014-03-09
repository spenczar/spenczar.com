Title: "How do I become a data scientist?"
Author: Spencer Nelson
Date: 2014-03-08 21:43:00
Slug: what-i-think-when-interviewing-data-scientist
Summary: What are startups looking for when they are hiring a data scientist?

I got an email recently asking something along these lines:

> I'm a smart ex-engineer who likes stats. I want to be a data
> scientist. How difficult will it be for me to find a job doing data
> science work at a startup?

I think a lot of people have this question. It's interesting that it's
common given how hard it is to find a quality data scientist. I sent
back an email which looked more or less like the following post -
these are my thoughts on how to get hired, as seen from the eyes of
someone who actually really wants to find more talented data
scientists to hire.

### Quantitative intuition

The first thing that I'm looking for is general quantitative
sense. This is a really low bar. It's not really important whether
someone knows the quirks of Cauchy distributions or whatever. All I
want is to see lots of confidence in thinking about things
quantitatively. Example things I'd talk about:

 - Which is better: doubling your week over week retention of users,
   or doubling the number of first-time visitors your site gets?
   
   (*answer*: retention, obviously - compounding interest is kind of a big deal)

 - Twitch has about 10,000 broadcasters online at any time, and about
   400,000 viewers at any time. What do you think the distribution of
   viewers across broadcasters would look like? Sketch a histogram,
   maybe? Which will be higher: mean or median?

(*answer*: they should expect a very steep concentration of viewers in
   a small set of channels, pretty much anyone who has been around
   large data sets quickly notices the
   [power law distributions](http://en.wikipedia.org/wiki/Zipf's_law)
   that show up everywhere)

### Programming skill

The second thing that I'm looking for is programming skill. This is
less important than quantitative sense, since it's easier to teach,
but teaching takes a lot of time so it's still pretty
important. Again, not looking for a whole lot here, mostly willingness
to get their hands dirty. Example questions:

- We've got 2 million log lines in a text file, I want you to pull out
  ones for the IP address 61.22.33.4. Don't overthink it.

(*answer*: I'm really checking that they don't overthink it here -
  simple, direct solutions are what we want. This is a really simple
  problem and they should recognize that, not hem and haw or try to be
  cute. Regex, subtring matching with python, perl, grep - all are
  fine. The point is whether you recognize that it's simple.)

- How much SQL do you know? Ever used mapreduce? Ever used AWS? Use
  python much? Do you spend time in R?

(*answer* I don't expect anyone to say yes to all of these or
  anything - this just points to breadth of experience, and more
  importantly it predicts how quickly they could start doing real
  work, because that summarizes our toolset pretty well)


### Business knowledge

The third thing is business knowledge and creativity. This is hard to
evaluate, but it's probably the most important facet. Depth of
knowledge in our industry is tremendously helpful: it lets someone put
their numbers in context and give them a sense of what's
reasonable.

And that's pretty crucial. It's really dangerous to have a data
scientist who doesn't know what "reasonable" is - they have a tough
time identifying bugs or bad data.

For this I usually just ask them to talk a little about what they'd be
interested in researching in their first few months at twitch. Bad
answer: "I want to use ensemble methods incorporating deep learning to
make recommendations!" Good answer: "I want to figure out what
differentiates successful League of Legends broadcasters from
unsuccessful ones!"


### Oh yeah, and also the usuals

The whole time, I'm also trying to evaluate some intangibles, like

 - Is this person really smart? Like, do they seem like one of the
   smartest people I've ever met? This is obviously hard to figure out
   in a brief interview, but when it's obvious, that's a good sign.
 - Could I imagine this person being easy to work with for just about
   everyone else in the company? This is a much more stringent
   requirement than you usually see for this dimension - data
   scientists have to talk with just about everyone all the time
   though, at least at Twitch.
 - Does this person have quiet confidence? Show-offs are bad news,
   especially for data science - you really don't want someone who is
   eager to prove that they know fancy algorithms. Data science is
   mostly sausage making - I want someone who exhibits a healthy dose
   of self-doubt, balanced by the confidence required to dive in and
   research things that they believe are important. It's a tricky
   tightrope to walk.


### Nobody is perfect

This might be an intimidating list of requirements at a glance, but I
don't think the bar is very high in any area, really. The hard part is
finding someone who is reasonably good in all three areas.

Most startups need generalist data scientists; Kaggle champs who do
tons of machine learning just don't have enough work to do at a
startup, and analysts who can't program will need too much support to
be a net positive. So, the goal is breadth of skills more than
anything. I'd bet it's different at much larger companies than
Twitch - that's just my experience.

That said, the ideal is a T-shaped person who is waaaaay better than
anyone else on the current team in at least one area so that they can
help us all get better.


### Be a generalist!

Anyways, I hope that gives you some sense of the way I think about
things when looking for somebody. I don't think every company would
have the same criteria as me - smaller companies will care more about
generalism and gumption, while larger companies will look for more
specialized people who do one axis particularly well, but I think the
overall scheme is pretty common.

Now is a good time to slip in the ad: Twitch is
[hiring like crazy](http://www.twitch.tv/p/jobs)! It's a great place
to work, you'd love it here. Seriously.

So drop me a line: <s@spenczar.com> (PS: We're looking for data
engineers too, not just science-y analyst types!)
