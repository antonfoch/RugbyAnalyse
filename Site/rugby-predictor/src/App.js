import React, { Component } from 'react';
import axios from 'axios';
import Loading from 'react-loading';
import Confetti from 'react-confetti';
import './App.css';

class RugbyPredictor extends Component {
  constructor() {
    super();
    this.state = {
      homeTeam: '',
      awayTeam: '',
      prediction: '',
      loading: false,
      confettiActive: false,
    };

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
    this.setState({ loading: true });

    setTimeout(() => {
      axios.post('http://127.0.0.1:5000/predict', { home_team: homeTeam, away_team: awayTeam })
        .then((response) => {
          this.setState({ prediction: response.data.winning_team, loading: false });
        })
        .catch((error) => {
          console.error(error);
          this.setState({ loading: false }); // Arrêt du chargement en cas d'erreur
        });
    }, 4000);
  }

  render() {
    return (
      <div className="RugbyPredictor">
        <h1 className='RugbyTitle'>Rugby Match Predictor</h1>
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
          <div className='middle'>
            <button onClick={this.handlePredictClick} className='predictbutton'>Predict Result</button>
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
        <div className='resultcontainer'>
          {this.state.loading ? (
            <Loading type="spinningBubbles" color="#007bff" height={50} width={50} />
          ) : (
            this.state.prediction && (
              <div>
                <Confetti numberOfPieces={200} />
                <p className='result'>Winner: {this.state.prediction}</p>
              </div>
            )
          )}
        </div>
      </div>

    );
  }
}

export default RugbyPredictor;
