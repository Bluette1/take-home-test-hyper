## Correctness
 - The code does not produce the expected output
 - You should not use a loop to solve the problem (Read instructions!)
 - Use Test Driven Development (TDD) to ensure correctness - Test code with examples of common types of pets, namely cat, dog, rabbit, hamster, budgie and parrot

  - You can install a testing gem such as `minitest` by running `gem install minitest` and then run corresponding tests 

    ```
    ruby spelling_checker_test.rb
    ```
  - Test as many scenarios as possible

  Suggested fix:
  - Use the [`map`](https://www.rubyguides.com/2018/10/ruby-map-method/) function instead of `each`. 
    - Change 
    ```
    array.each{ |n|
      if @words.include? n
        "*#{n}*"
      end
    }.join(' ')
    ```
    to 
    ```
      array.map { |n|
        if @words.include? n
          "*#{n}*"
        else
          n
        end
    }.join(' ')
    ```

## Efficiency
 
  -The constructor should take in parameters, so as to generalize the spell checker.

  Change
  ```
  def initialize
   @words = %w[catt ct caaat tcat]
  end
  ``` 
  to
  ```
    def initialize (words = %w[catt ct caaat tcat])
    @words = words
  end
  ```
## Style 
- Use camel case for class names (standard convention)

  -` class Spelling_Checker -> class SpellingChecker`

- Avoid using `{...}` for multiline blocks
  - Instead of  
  ```
  array.map { |n|
      if @words.include? n
        "*#{n}*"
      else
        n
      end
    }.join(' ')

  ```
  use 
  ```
  array.map do |n|
      if @words.include? n
        "*#{n}*"
      else
        n
      end
    end.join(' ')
  ```

  ## Documentation
  - Add comments(such as method definition) to explain what algorithm or method you are using to solve the task
  - Using comments to explain snippets of code will make your code easier to read and debug