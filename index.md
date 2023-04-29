---
layout: default
---

### **BACKGROUND**

As the world population has grown rapidly, there has been a need for faster and newer technologies to feed the people. One way to increase agricultural yield is to use nitrogen fertilizers. However, recent studies have shown that most of the nitrogen fertilizer applied to fields leaches into surface water bodies, causing pollution. Therefore, it is important to quantify the amount of nitrate load that leaches into surface water bodies.


This is important because nitrate pollution can have a number of negative impacts on human health and the environment. For example, nitrate pollution can contaminate drinking water, leading to health problems such as methemoglobinemia (blue baby syndrome) in infants. Nitrate pollution can also harm aquatic ecosystems, leading to algae blooms and fish kills.


Quantifying the amount on nitrate that leaches into surface water bodies will help policymakers, scientists, and the general public. Policymakers can use this information to make decisions about agricultural practices and water quality regulations. Scientists can use this information to study the impacts of nitrate pollution on human health and the environment. The general public can use this information to make informed decisions about their own health and the health of their environment.


### Water Pollution 

![Octocat](https://img-aws.ehowcdn.com/877x500p/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/f156a8535b7844d3996689ec37292370.jpg?type=webp)
**Figure 1** shows nitrate being deliverd into surface water through drain pipes


![dead fishes](https://www.iwla.org/images/default-source/conservation/water/nitrate-watch/algal-bloom---credit-getty-images.png?sfvrsn=745b9a0d_2)
**Figure 2** shows the loss of auqtic life as a result of nitrate pollution



* * *
### Factors contributing to nitrate pollution to surface water bodies
*   Nitrogen surplus
*   Precipitation
*   Streamflow


* * *
### **ANALYSIS**
Measuring nitrate concentration is very expensive and labor intensive so there are very little gauges that measure nitrate concentration across the state of Iowa, therefore this analysis seeks to investigate this factors affecting nitrate concentration in a region rich in data. The results of this analysis will use the relationship between contributing factors help predict nitrate concentration in areas where there no gauges.

# Correlation between streamflow and concentration 
To understand the relationship between streamflow and nitrogen concentration, we calculate the correlation between these two parameters

```js
// Python code calculating correlation between streamflow and Nitrate concentration at north racoon river at Sac city.
correlation = np.corrcoef(flow["streamflow"], concentration["nitrate"])[0, 1]
print("The correlation coefficient between streamflow and concentration is", correlation)
```


Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://img-aws.ehowcdn.com/877x500p/s3-us-west-1.amazonaws.com/contentlab.studiod/getty/f156a8535b7844d3996689ec37292370.jpg?type=webp)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
