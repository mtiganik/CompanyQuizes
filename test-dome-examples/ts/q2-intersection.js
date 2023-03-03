function fetchResource() {
    return {
        open: function () { console.log('opening'); },
        dispose: function () { console.log('disposing'); },
        "delete": function () { console.log('delete'); }
    };
}
function isDeleteable(openable) {
    return openable["delete"] !== undefined;
}
var resource = fetchResource();
if (isDeleteable(resource)) {
    resource["delete"]();
}
else {
    resource.dispose();
}
