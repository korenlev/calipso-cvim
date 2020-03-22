const ApiConnect = async (route:string,req:any) => {
  try {
    const res = await fetch(`http://64.103.124.101:4321/${route}`, {
    method: 'POST',
    body: JSON.stringify(req),
    headers: {
      'Content-Type': 'application/json'
    }
  })
  return res.json()
  } catch(error) {
    throw new Error("Whoops! "+error);
  }
}

export {ApiConnect}