var __assign = (this && this.__assign) || function () {
    __assign = Object.assign || function(t) {
        for (var s, i = 1, n = arguments.length; i < n; i++) {
            s = arguments[i];
            for (var p in s) if (Object.prototype.hasOwnProperty.call(s, p))
                t[p] = s[p];
        }
        return t;
    };
    return __assign.apply(this, arguments);
};
var Person = /** @class */ (function () {
    function Person() {
    }
    return Person;
}());
var first = { hair: "brunette", height: "173cm" };
var second = { eyeColor: "blue", height: "192cm" };
var third = { hair: "blonde" };
var person = __assign(__assign(__assign({}, first), second), third);
console.log(person);
