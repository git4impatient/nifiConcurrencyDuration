# nifiConcurrencyDuration
Search the nifi config for excessive concurrentlySchedulableTaskCount - if desired update to lower value and increase processor duration

(c) copyright 2023 Martin Lurie - this is sample code not supported

Why on earth would you want to reduce concurrency, surely this will make your Nifi flow slower????

Well...  it turns out you can slow your flow down by asking for more resources than you have.  

Please see Mark Payne Nifi Anti-Patterns on YouTube, at around 10 minutes he explains that concurrentlySchedulableTaskCount > 12 is an anti pattern.

https://www.youtube.com/watch?v=pZq0EbfDBy4

WARNING - DO NOT RUN THIS AGAINST PROD WITHOUT LOTS OF TESTING
DON'T EVEN THINK ABOUT RUNNING IT ON PROD WITHOUT LOTS OF TESTING

To run the script use:  bash goReduceConcurrency.sh

To undo the changes use: goUNDO

If you run the scripts without editing them and understanding them you will not be pleased with the outcome.

What does goReduceConcurrency.sh do?  There are 3 stages
- the first stage examines the Nifi flows and reports on xx yy
- stage two gets the current version of all the processors from the nifi-api, you need current version to make changes
- stage three does the actual updating using a threshold value that you can modify. Eg: every stage with concurrency greater than X gets reduced to concrency Y


Step by Step
- before you can run the script you need to download the flow definition in json format. Right click on the top level canvas to download everything.
-
-   Todo:
ToDo
- add descrition of attached scripts
- this will not handle a process group that only has processors - it needs a sub-process group

Many thanks to John K for all his help on this topic!
