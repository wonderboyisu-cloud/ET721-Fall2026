Isaam Shah
Professor Huixin Wu
ET 721
11/15/2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

* What was the initial test coverage? 
    Initial test coverage was 55 percent.

* What is the final test coverage you were able to achieve? 
    The final test coverage I was able to achieve was 100 percent.

* How many tests did you end up having?
    I ended up having 28 tests passed.

## Untested Code: Effects

* Were you able to understand all features and different use cases of the code without the tests? 
    The tests done in test_model.py were easier to understand than the tests in test_api.py.

* What did you think of having to test the API manually? 
    I think it was hard to write many lines to test the API manually.

* What was the result of having few tests on your understanding of the API?
    We didn't full coverage with pytest with the few tests that were present in test_api.py.

## Adding Tests

* How did you go about adding more tests to the code?
    I followed the instrcutions of what tests were required and how much coverage was left out

* What is the difference between a unit test and an API test? Do they bring different values?\
    A unit test checks one small piece of code in isolation, while an API test checks the application through its public HTTP interface. While a unit test checks

    Yes, and they complement each other. Unit tests give fast, precise feedback on the logic. API tests give confidence that the pieces work together the way a user would experience them. In this project, the unit tests alone left routes.py at 46% coverage because none of them touched the routes. Adding the API tests brought it to 100%. Neither type alone would have given full coverage.

## Automation

* What were the benefits of automating test coverage?
    Running coverage run -m pytest and coverage report -m showed me exactly which lines were untested, so I didn't have to guess what to test next. It also let me re-run every test in seconds after each change and see the coverage percentage go up.

## New Features

* What was your experience like having to add new features when you tested baseline code?
        Having tests in place first made adding features easier, because I could see how the existing code was supposed to behave before changing it.


* Did it give you any feeling of security when trying out new features?
    Yes. If a new feature broke something, the existing tests would fail right away, so I could fix it before it became a bigger problem.

## Future

* What do you hope to takeaway from the experience having to write tests?
    I hope to make testing a regular habit instead of an afterthought. Writing tests helped me understand the code better and showed me edge cases I would have missed, like empty lists and missing values.