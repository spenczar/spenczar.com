Title: The seven stages of startup analytics grief
Author: Spencer Nelson
Date: 2013-09-07 20:00:00
Slug: seven-stages-analytics-grief
Summary: Web apps seem to graduate through a series of stages with regards to analytics.

Web apps seem to graduate through a series of stages with regards to analytics. 

### Stage 1: We should probably keep track of page views, you guys
The "is this thing on?" phase. 

Most people start with Google Analytics or something like it. Nobody is looking for a lot of depth in the numbers - all you want to know is whether people are using your adorable little web app or reading your blog or whatever. Basically, this is about seeing whether you need to do a better job promoting yourself.

There's probably somebody in the company who compulsively checks on how many visitors you've got. Nobody really knows what they're looking for, but 10,000-visitor days from being on the front of Hacker News get everyone excited.

### Stage 2: We should probably track signups, too, you guys
The "okay we're ready for the users now" phase. 

You've got at least a thousand visitors per month probably, but not a lot of actual users, and you want to know why. You might use Google Analytics for this again, or maybe something like Mixpanel which supports richer data.

There's no really clear goal, but people are pretty sure that knowing more about who is signing up sounds like a good thing. So, you add some tracking to know more about who the users are that sign up.

### Stage 3: I think we should do some A/B tests
The "our product is great why aren't people signing up?" phase. 

You've now got a steady stream of visitors, and dedicated users sure seem happy (possibly because they get a ton of attention) but you're having a hard time converting visitors into dedicated users. Somebody read that A/B tests are pretty sweet on Patrick Kalzumeus's blog, and decides to do it. Google Analytics and Mixpanel don't really support this, so you throw Optimizely on the page.

The A/B tests are probably helpful, but not earth-shattering. Quietly, there's a lot of technical complexity accumulating: you track page views in Google Analytics, signups in MixPanel, and signups *again*, but only for A/B testing, in Optimizely. Gulp.

### Stage 4: We need to know a lot more about how people use our products
The "hmmm maybe we should go back to working on product and not the signup page" phase. 

You've now got enough users that it's not feasible to stay in close contact with everybody, and you're surprised by occasional negative comments on Hacker News. "Why didn't they just email me first?", you whinge. "We should add instrumentation all over our app, so we know how people actually use it and see what the problems are!"

Most of the instrumentation is done in Mixpanel, but page views are still in GA. Things are getting sufficiently complex that there's one engineer who is just known as "the analytics guy" and who has become the local expert on the quirks and warts through pure accident.

### Stage 5: We need to use all this data better
The "lets hire a data scientist" phase. 

You've got a pile of data sprawled across three different systems. It's been added haphazardly and incrementally, with new metrics thrown in to judge particular A/B tests, and without any particularly clear owner. Now, no single person in the company understands all the data you collect fully - everyone understands only a small piece. You're getting the sense that if someone were analyzing it full-time, there might be a lot of extra info value in there.

This is a big turning point. In stages 1-4 there's unimpeded, organic growth of analytics, and now it will finally get pruned back a bit and organized. The new data analyst probably complains a lot about data quality and coverage, but at least someone is finally noticing that that's become a real problem. 

### Stage 6: We need to do our own analytics
The "time to set up a hadoop cluster" phase. 

You've got a lot of data, and you've got a full-time analyst, but these third-party analytics providers just aren't cutting it. To be fair, they aren't built for the volume of data you're pushing to them at this point - wide instrumentation all over a well-trafficked site can be heavy. Your data scientist is probably also telling you that she needs much more horsepower to do valuable analysis, and building your own systems for this is starting to sound attractive.

Now you're starting to look at a data *team*. This is part of the continuing consolidation of data into a stable system (as opposed to its rapid expansion earlier). Those disparate systems gradually get some cohesion.

### Stage 7: We should turn our analytics into features for users
The "lets build a recommendation engine" phase. 

Once you've got a data team, complete with engineers and infrastructure for mining significance out of billions of data points, someone realizes that this should be used in (nearly) real-time systems to benefit users. 

This is a very large project, since real-time data is quite different from the static analysis you've been doing with very different engineering challenges, and the data team might even split into two sub teams here. With a little luck, though, the data systems become a feature - and a powerful competitive advantage. Your data systems will be hard for any startup competitor to duplicate since they won't have the accumulated data points to make good decisions.

* * *

### Moral of the story: It's hard to manage data quality
There's one big theme to this I want to get at: it's tough to maintain a high-quality data system.

For a while in the beginning, it feels easy - you only have a few people in the company so everyone knows what all of your metrics mean, and there aren't many of them anyway, and they're pretty straightforward since your product hasn't gone through many iterations. But two years later, you look up and realize that data quality has gone off the rails. So there's this burst of expansion, and then a consolidation phase afterwards.

It's not a coincidence that this mirrors the pattern of most startups' codebases, which go from simple to harebrained as the product evolves, and two years later people grumble that maybe we should just rewrite this whole thing.

The difference is that your codebase has a CTO. It has an owner. That owner is responsible for its quality, which helps hold things together (optimistically!). Few teams start with a Chief Data Officer, though. Usually, analytics is a side-concern, a means to an end, and it is nobody's top priority, which is all completely justified but which results in a bit of chaos.

Again, to be clear, I think that's fine, it's just something to watch out for. I think as data becomes a more core component of businesses, we'll see an evolution of data management best practices, something like the evolution of best practices in web development over the past 20 years.

[Discuss this on Hacker News](http://spenczar.com/posts/2013/Sep/07/seven-stages-analytics-grief/). Or, email: <s@spenczar.com>
