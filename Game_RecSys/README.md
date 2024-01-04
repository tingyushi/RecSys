# Game Recommendation System

### Hours Prediction
* Predict if a player would play a certain game
* Latent Factor Model ($\alpha$ and $\beta$ model)

### Would Play Prediction
* Predict how many hours a player would play a game
* BPR using tensorflow + Logistic Regression

### Baseline Methods
* Hours Prediction: Compute averages for each user, or return the global average if we've never seen the user before
* Would Play Prediction: Just rank which games are popular and which are not and return '1' if a game is among the top-ranked