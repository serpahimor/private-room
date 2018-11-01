import React, { Component } from 'react';
import LatestActivity from './components/LatestActivity';

export default class Page2 extends Component {
  static displayName = 'Page2';

  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="page2-page">
        <LatestActivity />
      </div>
    );
  }
}
