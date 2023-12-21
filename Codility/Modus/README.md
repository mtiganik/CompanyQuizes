Codility tests I did when I applied to Proxify. They named tests as Javascript tests, but it was pure React (wrong preparing gahh). Codility gave 3 pure code writing tests and 3 hours to solve. They were difficult. Solutions are both here in main folder and in React folder. 

''Task No 2:''
Your task is to implement a component displaying a lazily loaded image gallery in React.

Requirements:
*Component should accept an 'images property, which is an array of image URLs for the gallery.
* Use the 'img' element to display the images. Ensure that you also use img for images that aren't loaded yet (img with empty src attribute)
*arrange the images in a three-column grid with 200px by 200px cells
* Implement lazy loading so that an image in the gallery should be loaded once the image is 100px or less below the visible viewport (below the fold)

Assumptions:
*The images property always contains an array of working image URLs
*All images in the images property have dimensions of 200px width and 200px height

Hints:
*IntersectionObserver might be useful
*Do NOT use React.lazy, this task is about lazy loading images not code splitting

// initial code:

import React from "react";

function ImageGallery({ images }) {

return(
<div>code here </div>
) 
}

export default ImageGallery;




''Task No 3:''
Your task is to implement a React component that renders a table with pagination.

1. The table has class name table and contains three columns: 'ID', 'First Name' and 'Last Name'. It is populated with data that can be fetched from mocked https://example.com/api/users endpoint. The endpoint requires one query parameter: 'page' (with zero based numbering, if you do not provide this parameter, the API will return an error). This is an example of a response formatted using JSON:

{
"count":13,
"results":[
    { "id":1, "firstName":"Bob", "lastName":"Wallace"},
    { "id":1, "firstName":"Sonya", "lastName":"Ross"},
    { "id":1, "firstName":"Anthony", "lastName":"Thomson"}

]
}
counts value points to the total number of results, whereas results contains items from the given page. The page size equals 10. The last page of data might be smaller. If a request is sent with the query param page larger than the total number of pages, then results will be empty.
2. Initially, the table 'tbody' should be populated with the first page of data.
3. The pagination section has class name 'pagination and consists of four buttons which are stacked horizontally.
*Clicking the first button navigates to the first page of data, wereas clicking the second button navigates to the previous page of data. The buttons become disabled either when the current page is the first page or when a page of data is currently being loaded. The buttons have (respectively) 'first-page-btn' and 'previous-page-btn' class names
*Similarly, clicking the third button navigates to the next page of data, whereas clicking the last button navigates to the last page of data. The buttons become disabled same way as first two buttons.
*The content of the buttons should be (respectively) 'first','previous', 'next' and 'last'
4.while data is being loaded, all buttons should be disabled
5. The component should be the default export and can be either a function or a class.
6. Use Fetch API for making requests.
7. Please remember to use 'tbody' when rendering data.

https://example.com/api/users is a mocked service. It will not fail when the page query parameter is provided

// Initial code:
import React from 'react';

const USERS_URL = 'https://example.com/api/users';

export default function Table () {
  return (
    <div>
      <table className="table">
        <thead>
          <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
          </tr>
        </thead>
        <tbody>
        //  render elements in tbody
        </tbody>
      </table>
      <section className="pagination">
        <button className="first-page-btn">first</button>
        <button className="previous-page-btn">previous</button>
        <button className="next-page-btn">next</button>
        <button className="last-page-btn">last</button>
      </section>
    </div>
  );
};

