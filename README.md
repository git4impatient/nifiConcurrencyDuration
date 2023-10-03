# nifiConcurrencyDuration
Search the nifi config for excessive concurrentlySchedulableTaskCount - if desired update to lower value and increase processor duration

(c) copyright 2023 Martin Lurie - this is sample code not supported

Why on earth would you want to reduce concurrency, surely this will make your Nifi flow slower????

Well...  it turns out you can slow your flow down by asking for more resources than you have.  

Please see Mark Payne Nifi Anti-Patterns on YouTube, at around 10 minutes he explains that concurrentlySchedulableTaskCount > 12 is an anti pattern.

https://www.youtube.com/watch?v=pZq0EbfDBy4

ToDo
- add descrition of attached scripts
- debug this error message parse error: Invalid numeric literal at line 1, column 31416

