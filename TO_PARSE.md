# Hints on how to parse html in python

install pyquery

get body of response from response object from request and feed it into pyquery

You can try out jQuery-like selectors in the developer console of any browser: (this is JS but the same css selectors will work in pQuery)

```
document.querySelector('meta[name=robots]')

<meta name="robots" content="noindex">
```

i.e. matches meta tags with attribute "name" with value "robots".


You then want the content attribute: in JS this is:

```
document.querySelector('meta[name=robots]').getAttribute('content')

"noindex"
```

(find equivalent .getAttribute for puquery)


don't forget error handling along the way - is there a meta tag? then proceed, otherwise not


## pseudocode

content = response.body()
pQuery = pq.load(content)
metaRobots = pQuery('meta[name=robots]')
if (metaRobots is not nil):
  meta_robots_content = pQuery(metaRobots).getAttribute('content')
