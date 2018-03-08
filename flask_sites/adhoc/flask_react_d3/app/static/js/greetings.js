var realPython = React.createClass({
  render: function() {
    return (<h2>Greetings, from React Python!</h2>);
  }
});

ReactDOM.render(
  React.createElement(realPython, null),
  document.getElementById('greetings_content')
);
