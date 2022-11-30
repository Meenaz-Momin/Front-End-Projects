import { useContext } from "react";
import EmpContext from "./Context";
function Display() {
  const { tableList, handleDelete, handleEdit } = useContext(EmpContext);

  return (
    <div className="display">
      <table>
        <thead>
          <tr>
            <th>Emp. ID</th>
            <th>Name</th>
            <th>Mobile No.</th>
            <th>Designation</th>
            <th>Address</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {tableList.map((user, i) => {
            return (
              <tr key={i}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.number}</td>
                <td>{user.designation}</td>
                <td>{user.address}</td>
                <td>
                  <button className="btn2" onClick={() => handleEdit(user)}>
                    Edit
                  </button>
                  <button
                    className="btn2"
                    onClick={() => handleDelete(user.id)}
                  >
                    Delete
                  </button>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}

export default Display;
