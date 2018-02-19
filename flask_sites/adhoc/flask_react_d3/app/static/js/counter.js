/*** @jsx React.DOM */

var realPython = React.createClass({
    constructor(props) {
      super(props);
      this.state = { seconds: 0 };
    }

    tick() {
      this.setState(prevState => ({
        seconds: prevState.seconds + 1
      }));
    }

    componentDidMount() {
      this.interval = setInterval(() => this.tick(), 1000);
    }

    componentWillUnmount() {
      clearInterval(this.interval);
    }

    render: function() {
      return (<h2>"Seconds: "</h2>);
      );
    }
  }
});

ReactDOM.render(
  React.createElement(realPython, null),
  document.getElementById('content')
);
