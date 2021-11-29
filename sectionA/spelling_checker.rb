# Use camel case for class names (standard convention)
# class Spelling_Checker
class SpellingChecker
  # def initialize
  #   @words = %w[catt ct caaat tcat]
  # end
  # The constructor should take in parameters, so as to generalize
  # the spell checker
  def initialize(words = %w[catt ct caaat tcat])
    @words = words
  end

  def spellChecker(string)
    array = string.split(' ')

    # array.each{ |n|
    # if @words.include? n
    #   "*#{n}*"
    # end
    # }.join(' ')

    # First of all you should not use a loop to solve the problem (Read instructions!)
    # Use Test Driven Development (TDD) - Test code with examples of common types
    #  of pets, namely cat, dog, rabbit, hamster, budgie and parrot
    
    # Avoid using `{...}` for multiline blocks
    # array.map { |n|
    #   if @words.include? n
    #     "*#{n}*"
    #   else
    #     n
    #   end
    # }.join(' ')
    array.map do |n|
      if @words.include? n
        "*#{n}*"
      else
        n
      end
    end.join(' ')
  end
end

# checker = SpellingChecker.new
# checker = SpellingChecker.new()
# output = checker.spellChecker('cat ct')
# Add extra tests
# checker = SpellingChecker.new(%w[dogg dg dooog gdog])
# output = checker.spellChecker('dog dg')
checker = SpellingChecker.new(%w[rabbitt rabit raaaabit trabbit])
output = checker.spellChecker('rabbit rabit')
p output

# Add comments(such as method definition) to explain what algorithm or method you are using to solve the task
# Using comments to explain snippets of code will make your code easier to read and debug
