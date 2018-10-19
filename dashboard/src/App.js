import React, { Component } from 'react';
import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/css/bootstrap-theme.css';
import './App.css';

import { Navbar, Button, ButtonToolbar, ButtonGroup, DropdownButton, MenuItem } from 'react-bootstrap';
import $ from 'jquery';

const buttonClickLivingRoomLightsOff = function(event){
  $.ajax({
    method: 'GET',
    url: 'http://maker.ifttt.com/trigger/living_room_lights_off/with/key/bxjBy8urzzYOWphww44iI6',
    dataType: 'jsonp'
  })
}

const buttonClickLivingRoomLightsOn = function(event){
  $.ajax({
    method: 'GET',
    url: 'http://maker.ifttt.com/trigger/living_room_lights_on/with/key/bxjBy8urzzYOWphww44iI6',
    dataType: 'jsonp'
  })
}

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h2>Dashboard</h2>
        </div>
        <ButtonGroup>
          <DropdownButton id="dropdown-btn-menu" bsStyle="success" title="LR Lights">
            <Button bsStyle="info" onClick={buttonClickLivingRoomLightsOff}>Off</Button>
            <Button bsStyle="info" onClick={buttonClickLivingRoomLightsOn}>On</Button>
          </DropdownButton>
          <Button bsStyle="info">Middle</Button>
          <Button bsStyle="info">Right</Button>
        </ButtonGroup>
      </div>
    );
  }
}

export default App;
