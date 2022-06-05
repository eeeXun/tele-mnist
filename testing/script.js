import http from "k6/http";
import {sleep} from "k6";

const img = open("test.png", "b");
const url = "http://10.22.23.22:5000"
const data = {
    img: http.file(img),
};

export let options = {
    vus: 10,
    duration: "10m",
};

export default function() {
    http.post(url, data);
    sleep(5);
}
