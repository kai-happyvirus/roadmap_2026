---
layout: page
title: Blog
permalink: /blog/
---

# Learning Logs

Daily reflections, insights, and "aha!" moments from my 180-day ML/CUDA/LLM journey.

<div class="posts">
  {% for post in site.posts %}
    <article class="post">
      <h2><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h2>
      <div class="entry">
        {{ post.excerpt }}
      </div>
      <div class="meta">
        <span class="date">{{ post.date | date: "%B %d, %Y" }}</span>
        <span class="tags">
          {% for tag in post.tags %}
            <span class="tag">{{ tag }}</span>
          {% endfor %}
        </span>
      </div>
      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More →</a>
    </article>
  {% endfor %}
</div>
