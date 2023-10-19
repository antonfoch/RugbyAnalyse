import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class RugbyPredictor extends Component {
  constructor() {
    super();
    this.state = {
      homeTeam: '',
      awayTeam: '',
      prediction: '',
    };

    // Tableau des équipes
    this.teams = ['Argentina', 'Australia', 'England', 'France', 'Ireland', 'Italy', 'New Zealand', 'Scotland', 'South Africa', 'Wales'];
  }

  handleHomeTeamChange = (event) => {
    this.setState({ homeTeam: event.target.value });
  }

  handleAwayTeamChange = (event) => {
    this.setState({ awayTeam: event.target.value });
  }

  handlePredictClick = () => {
    const { homeTeam, awayTeam } = this.state;

    // Effectuez une requête HTTP POST vers l'API Flask
    axios.post('http://127.0.0.1:5000/predict', { home_team: homeTeam, away_team: awayTeam })
      .then((response) => {
        this.setState({ prediction: response.data.winning_team });
      })
      .catch((error) => {
        console.error(error);
      });
  }

  render() {
    return (
      <div className="RugbyPredictor">
        <h1 className='RugbyTitle'>Rugby Match Predictor</h1>
        <div className='Container'>
          <div className='OptionContainer'>
            <div className='Home'>
              <label>Home</label>
              <select onChange={this.handleHomeTeamChange}>
                <option value="">Select a team</option>
                {this.teams.map((team, index) => (
                  <option key={index} value={team}>{team}</option>
                ))}
              </select>
            </div>
            <div>
              <p>VS</p>
            </div>
            <div className='Away'>
              <label>Away</label>
              <select onChange={this.handleAwayTeamChange}>
                <option value="">Select a team</option>
                {this.teams.map((team, index) => (
                  <option key={index} value={team}>{team}</option>
                ))}
              </select>
            </div>
          </div>
          <button onClick={this.handlePredictClick}>Predict Result</button>
          {this.state.prediction && (
            <div>Result of the prediction: {this.state.prediction}</div>
          )}
        </div>



      </div>
    );
  }
}

export default RugbyPredictor;
