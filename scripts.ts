interface H3Element extends HTMLElement {
    tagName: 'H3';
}

interface ImageElement extends HTMLElement {
    tagName: 'IMG';
    alt: string;
    src: string;
    width: number;
    height: number;
}

interface ParagraphElement extends HTMLElement {
    tagName: 'P';
}

interface AnchorElement extends HTMLElement {
    tagName: 'A';
    href: string;
    target: string;
    text: string; 
}

interface JSONFILETYPE extends JSON {
    title: string,
    image_link: string,
    description: string,
    blog_link: string
}


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
            i++
            }
        }
        populate_latest(data['latest']);
        let one = getRandomIndex(count);
        let two = getRandomIndex(count);
        while (one == two){
            two = getRandomIndex(count);
        };
        display_random_posts(blog[`blog_${one}`], document.querySelector('.post_1') as HTMLDivElement);
        display_random_posts(blog[`blog_${two}`], document.querySelector('.post_2') as HTMLDivElement);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });

let getRandomIndex = (numbers: Array<number>) : number => {
    const randomIndex = Math.floor(Math.random() * numbers.length);
    return numbers[randomIndex];
}

const populate_latest = (jsn: JSONFILETYPE) => {
    let section = document.getElementsByClassName("latest-post");
    let title = section[0].children[0] as H3Element;
    let img_url = section[0].children[1] as HTMLElement;
    let description = section[0].children[2] as ParagraphElement;
    let post_url = section[0].children[3] as HTMLAnchorElement;
    title.innerHTML = jsn.title;
    img_url.setAttribute("src", jsn.image_link);
    description.innerHTML = `${jsn.description.slice(0, 300)}...`;
    post_url.setAttribute("href", jsn.blog_link)
}

const display_random_posts = (jsn: JSONFILETYPE, section: HTMLDivElement) => {
    let title = section.querySelector('h4') as H3Element;
    let img_url = section.querySelector('img') as HTMLElement;
    let description = section.querySelector('p') as ParagraphElement;
    let post_url = section.querySelector('a') as HTMLAnchorElement;
    title.innerHTML = jsn.title;
    img_url.setAttribute("src", jsn.image_link);
    description.innerHTML = `${jsn.description.slice(0, 200)}...`;
    post_url.setAttribute("href", jsn.blog_link)
}