import http from "k6/http";
import {sleep} from "k6";

const img = open("test.png", "b");
const url = "http://branko.lab.test.ncnu.org:5000"
const data = {
    img: http.file(img),
};

export default function() {
    http.post(url, data);
    sleep(1);
}
