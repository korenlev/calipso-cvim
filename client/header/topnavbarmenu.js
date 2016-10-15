Template.topnavbarmenu.events = {
    "keypress #search": function  (event,template) {
        if (event.which === 13) {
            var instance = Template.instance(),
                findFromParent =  instance.$(event.target).val();
            console.log("temp val is " + findFromParent);

            //var selectedVal = $('#search').val();
            var node = d3Graph.svg.selectAll(".node");
            if (findFromParent == "none") {
                node.style("stroke", "white").style("stroke-width", "1");
            } else {
                var selected = node.filter(function (d, i) {
                    return d.object_name.indexOf(findFromParent)<0;
                    //return d.name != findFromParent;
                });
                selected.style("opacity", "0");
                var link = d3Graph.svg.selectAll(".link")
                link.style("opacity", "0");
                d3.selectAll(".node, .link").transition()
                    .duration(5000)
                    .style("opacity", 1);
            }

        }
    },
};