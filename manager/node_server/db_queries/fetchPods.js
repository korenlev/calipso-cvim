const fetchBuildnodeMaster = async () => {
  try {
    conn = await pool.getConnection();
    return await conn.query(`select * from buildnode_master`);
  } catch (err) {
    throw err;
  }
}

module.exports = {
  fetchBuildnodeMaster,
};
