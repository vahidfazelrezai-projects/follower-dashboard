const fs = require('fs');
const app = require('express')();
const rs = require('rockset')(
  process.env.ROCK_API_KEY || fs.readFileSync('ROCK_API_KEY', 'utf8').trim(), 
  'https://api.rs2.usw2.rockset.com',
);

app.get('/followers', (req, res) => {
  rs.queries.query({
    'sql': {
      'query': `
        SELECT 
          handle, 
          ARRAY_AGG(ARRAY_CREATE(_event_time, followers)) data
        FROM yang.twitter_followers 
        WHERE _event_time > CURRENT_TIMESTAMP() - DAYS(7)
        GROUP BY handle
      `,
    }
  }, (err, response, body) => {
    if (err) {
      console.log(err);
      res.status(500).send(err);
    }
    res.send(response.results);
  });
});

app.listen(3000, () => console.log('server starting...'));
