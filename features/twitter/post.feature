Feature: Bora tweetá

    Scenario: Twitter hacker
        Given I am logged in as "fake-leticia"
        Then I should see the message "The email and password you entered did not match our records. Please double-check and try again."
    
    Scenario: Tweet like a crazy teenager
        Given I am logged in as "leticia"
        When I write the tweet "Restart não presta mais porque eu cheguei aqui 8 horas da manhã e eles não vieram falar com a gente. Não, eu não vou perdoar. Eu vou xingar no twitter hoje, muito. Sério."
        Then I should not be able to submit the tweet

    Scenario: Tweet like a pro
        Given I am logged in as "leticia"
        When I write the tweet "Eu vos escrevo estas cousas,... #selenium #python"
            And I press "js-tweet-btn" button
        Then I should see my tweet