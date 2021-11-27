# Run `gem install minitest` in the terminal inside the project folder 
begin
  gem 'minitest', '>= 5.0.0'
  require 'minitest/autorun'
  require 'minitest/pride'
  require_relative './spelling_checker'
rescue Gem::LoadError => e
  puts "\nMissing Dependency:\n#{e.backtrace.first} #{e.message}"
  puts 'Minitest 5.0 gem must be installed for the Ruby track.'
rescue LoadError => e
  puts "\nError:\n#{e.backtrace.first} #{e.message}"
  puts DATA.read
  exit 1
end

# require 'minitest/pride'

# Common test data version: 1.1.0 be3ae66
class SpellingCheckerTest < Minitest::Test
  
  def test_spelling
    scenarios = {
      a: ['cat *ct*', 'cat ct', %w[catt ct caaat tcat]],
      b: ['dog *dg*', 'dog dg', %w[dogg dg dooog gdog]],
      c: ['rabbit *rabit*', 'rabbit rabit', %w[rabbitt rabit raaaabit trabbit]]
    }

    scenarios.each_value do |scenario|
      @checker = SpellingChecker.new(scenario[2])
      expected = scenario[0]
      actual = @checker.spellChecker(scenario[1])
      assert_equal expected, actual
    end
    # assert_equal 'cat *ct*', @checker.spellChecker('cat ct')
    # assert_equal 'dog *dg*', @checker.spellChecker('dog dg')

  end

end

