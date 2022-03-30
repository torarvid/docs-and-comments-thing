# Documentation

## What's the scope of talking about documentation?

Well, we're a development team, so the purpose of this talk - documentation of
coding projects, and software/hardware that we use/run is what we're gonna talk
about.

There are different... "levels" in developer lyfe where it makes sense to talk
about documentation. You could for instance document:

* How we use coding conventions or do code reviews in the entire company
* A birds-eye view of what Alma is and how it works
* How trex interfaces with the Schäfer NGKP2 protocol
* What the AvisoClientException class is used for
* What the test_stripe_buffer unit test does

🤔 "Hey, wait a minute, you're suddenly talking about code comments now". Right
right, they are related, but let's start with focusing on documentation for
now...


We sometimes *write* documentation, and we sometimes *read* documentation.

## Reading documentation

### What experiences do we have when wanting to consume documentation?

* 👎 It doesn't exist at all
* 👎 It's obsolete
* 👎 It's written by somebody who doesn't remember what it's like to not know
  anything about the project
* 😐 It gets you started, but not where you need to be
* 😐 Not all of it is obsolete, but you don't know which part to trust and not
* 👍 It's clear and easy to understand (rare, but I guess it does happen)

## Writing documentation

### Why do we document how our systems work?

* 👎 It takes time
* 👎 It's not clear what you're getting
* 👎 It's (usually) boring
* 👍 It makes it possible for others to understand how things work
* 👍 It decouples code authors from new starters
* 👍 You might leave the company some day (or you know, die in a freak accident
  etc)

### My journey through life re documentation

1. I'm a developer, I want to write code, not documentation
2. I'm not a writer
3. People can just ask me how things work
4. Incidents happen and people don't understand how to fix
5. Ok, I'll write some notes
6. New people start and I spend way more time than I thought I would talking
   about how things work
7. I tell myself to get better at writing documentation in the future

### My journey with a new employer/team/project re documentation

Well, same as above, with a few changes perhaps... History repeats itself.

* Whenever we start something, it will usually be small/non-existing at the
  time, and it's easy to think "well, this is just a small thing for now, no
  need for docs yet... We don't even know how it will work yet, so
  documentation would be obsolete before we even start!"
* And then we continue from around point 3. above

(Noticing while I'm writing this, that there are similarities to other aspects
of developer lyfe, like writing tests, working with observability, monitoring
etc)

### Why is it so hard to get good at this?

Mentioned some of these points in the "why do we document" section, but one way
to try to summarize could be "there's almost always something that feels
valuable to do that is also much more fun to do than documenting".

### Can we get better at it?

* We could be more explicit about making documentation tasks when we're
  prioritizing work
  * This could include things like having a session with an outsider and get
    feedback on how well the documentation is understood
* We could talk more about it in an effort to engrain it into our culture as
  developers, but I have no idea whether that will work or not
* Maybe we need to accept that it will always be an area where people do "the
  least amount of work possible"
* We could attempt to formalize numbers that explain where we want the balance
  to be when it comes to writing/maintaining documentation vs other things. "We
  should use 5% of all of our time at work on documentation" or something like
  that (this would amount to around 2 hours per week)

### Where should we start spending our efforts?

Not sure, but how about some of these:

* Trex for dummies (how do you start out in our team? trex is a fairly
  specialized software suite that can feel intimidating to new developers)
* "Trex stories" or something
  * How a box goes from the boxing station to ending up on a pallet
  * What are vendor managers?
  * Adding a new HTTP endpoint and get it to work end-to-end with Alma
* How to work with GraphQL in Alma (not sure if this is still relevant)
