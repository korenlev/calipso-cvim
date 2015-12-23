'use strict';

window.Graph = window.Graph || {};

window.Graph.DataManager = new function () {
	this.getData = function(isTest)
	{
		return isTest ? testData : realData;
	}
	
	var testData = 
	{
		Entities:
		[
			{id:1, label: "Entity 1"},
			{id:2, label: "Entity 2"},
			{id:3, label: "Entity 3"},
		],
		Relations:
		[
			{"from":1,"to":2,"arrows":"to"},
			{"from":1,"to":3,"arrows":"to"},
			{"from":2,"to":3,"arrows":"to"},
		]
	};
	
	// this is what we got from server
	// it will be properly parsed and mapped in GraphManager
	var realData =
	{
		Entities:
			[
				{"id": "Jan4TenantDemo","label": "Jan4TenantDemo","group": "Jan4TenantDemo","attributes": {
					"Eth1": "192.168.55.4",
					"Eth0": "192.168.44.5",
				}},
				{"id": "Bridge1","label": "Bridge1", "group": "Jan4TenantDemo","attributes": {
					"port1": "taped1",
					"port2": "qvbed1",
				}},
				{"id": "Bridge2","label": "Bridge2", "group": "Jan4TenantDemo","attributes": {
					"port1": "taped2",
					"port2": "qvbed2",
				}},
				{"id": "OvsNode13","label": "OvsNode13", "group": "OvsNode13","attributes": {
					"port12": "taped1",
					"port30": "qvbed1",
				}},
				{"id": "Node13","label": "Node13","title": 'I have a popup!', "group": "OvsNode13","attributes": {
					"Eth0": "192.168.44.0",
				}},
			],

		Relations:
			[
				{ "from": "Jan4TenantDemo", "to": "Bridge1",label:'label demo',title: 'I have a popup!',"rootLevel":true,"approved": true},
				{ "from": "Jan4TenantDemo", "to": "Bridge2","rootLevel":true,"approved": true},
				{ "from": "Bridge1", "to": "OvsNode13","rootLevel":false,"approved": true},
				{ "from": "Bridge2", "to": "OvsNode13","rootLevel":false,"approved": true},
				{ "from": "OvsNode13", "to": "Node13","rootLevel":true,"approved": true},
			]	}
/*
	var realData =
	{
		Entities:
		[{"id":1,"group":"Supplier","label":"Supplier 1","archived":false},{"id":2,"group":"Supplier","label":"Supplier 2 ","archived":false},{"id":24,"group":"Agent","label":"Agent1","archived":false},{"id":3,"group":"Supplier","label":"Supplier 3","archived":false},{"id":15,"group":"Factory","label":"Factory 1 ","archived":false},{"id":27,"group":"SubContractor","label":"Sub Contractor 1","archived":false},{"id":16,"group":"Factory","label":"Factory 2","archived":false},{"id":28,"group":"SubContractor","label":"Sub Contractor 2","archived":false},{"id":29,"group":"SubContractor","label":"Sub Contractor 3","archived":false},{"id":26,"group":"SellingAgent","label":"Selling Agent 1","archived":false},{"id":7,"group":"Supplier","label":"Supplier","archived":false},{"id":19,"group":"Factory","label":"Factory 3","archived":false}],

		Relations:
		[{"groupid":480,"from":1,"to":2,"arrows":"to","label":"Contract To","approved":true,"archived":false,"rootLevel":true},{"groupid":478,"from":24,"to":1,"arrows":"to","label":"Introduces to owner","approved":true,"archived":false,"rootLevel":false},{"groupid":479,"from":1,"to":24,"arrows":"to","label":"Introduced to owner by","approved":true,"archived":false,"rootLevel":false},{"groupid":481,"from":1,"to":3,"arrows":"to","label":"Contracted By","approved":true,"archived":false,"rootLevel":false},{"groupid":482,"from":1,"to":15,"arrows":"to","label":"Owns","approved":true,"archived":false,"rootLevel":false},{"groupid":486,"from":15,"to":1,"arrows":"to","label":"Owned By","approved":true,"archived":false,"rootLevel":false},{"groupid":487,"from":15,"to":2,"arrows":"to","label":"Contracted By","approved":true,"archived":false,"rootLevel":true},{"groupid":488,"from":15,"to":27,"arrows":"to","label":"Sub Contract To","approved":true,"archived":false,"rootLevel":false},{"groupid":484,"from":1,"to":27,"arrows":"to","label":"Sub Contract To","approved":true,"archived":false,"rootLevel":false},{"groupid":490,"from":27,"to":1,"arrows":"to","label":"Sub Contracted By","approved":true,"archived":false,"rootLevel":false},{"groupid":491,"from":27,"to":15,"arrows":"to","label":"Sub Contracted By","approved":true,"archived":false,"rootLevel":false},{"groupid":492,"from":27,"to":16,"arrows":"to","label":"Owned By","approved":true,"archived":false,"rootLevel":false},{"groupid":483,"from":1,"to":16,"arrows":"to","label":"Contract To","approved":true,"archived":false,"rootLevel":false},{"groupid":493,"from":27,"to":28,"arrows":"to","label":"Sub Contract To","approved":true,"archived":false,"rootLevel":false},{"groupid":489,"from":15,"to":28,"arrows":"to","label":"Owns","approved":true,"archived":false,"rootLevel":false},{"groupid":494,"from":27,"to":29,"arrows":"to","label":"Sub Contracted By","approved":true,"archived":false,"rootLevel":false},{"groupid":485,"from":1,"to":26,"arrows":"to","label":"Represented By","approved":true,"archived":false,"rootLevel":false},{"groupid":495,"from":26,"to":1,"arrows":"to","label":"Represent","approved":true,"archived":false,"rootLevel":false},{"groupid":496,"from":1,"to":7,"arrows":"to","label":"Contract To","approved":true,"archived":false,"rootLevel":false},{"groupid":497,"from":2,"to":7,"arrows":"to","label":"Contract To","approved":true,"archived":true,"rootLevel":true},{"groupid":498,"from":2,"to":19,"arrows":"to","label":"Owns","approved":true,"archived":false,"rootLevel":true}]
	}
*/
};