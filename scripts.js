"use strict";
fetch('./blogs.json')
    .then(response => {
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    return response.json();
})
    .then(data => {
    const blog = data['blog'];
    let count = [];
    let i = 1;
    for (let prop in blog) {
        if (blog.hasOwnProperty(prop)) {
            count.push(i);
            i++;
        }
    }
    populate_latest(data['latest']);
    let one = getRandomIndex(count);
    let two = getRandomIndex(count);
    while (one == two) {
        two = getRandomIndex(count);
    }
    ;
    display_random_posts(blog[`blog_${one}`], document.querySelector('.post_1'));
    display_random_posts(blog[`blog_${two}`], document.querySelector('.post_2'));
})
    .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
});
let getRandomIndex = (numbers) => {
    const randomIndex = Math.floor(Math.random() * numbers.length);
    return numbers[randomIndex];
};
const populate_latest = (jsn) => {
    let section = document.getElementsByClassName("latest-post");
    let title = section[0].children[0];
    let img_url = section[0].children[1];
    let description = section[0].children[2];
    let post_url = section[0].children[3];
    title.innerHTML = jsn.title;
    img_url.setAttribute("src", jsn.image_link);
    description.innerHTML = `${jsn.description.slice(0, 300)}...`;
    post_url.setAttribute("href", jsn.blog_link);
};
const display_random_posts = (jsn, section) => {
    let title = section.querySelector('h4');
    let img_url = section.querySelector('img');
    let description = section.querySelector('p');
    let post_url = section.querySelector('a');
    title.innerHTML = jsn.title;
    img_url.setAttribute("src", jsn.image_link);
    description.innerHTML = `${jsn.description.slice(0, 200)}...`;
    post_url.setAttribute("href", jsn.blog_link);
};
