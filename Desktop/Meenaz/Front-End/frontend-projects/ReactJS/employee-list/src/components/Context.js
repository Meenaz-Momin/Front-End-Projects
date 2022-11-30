import { createContext, useState, useEffect } from "react";

const EmpContext = createContext();

export const EmpProvider = ({ children }) => {
  const [edit, setEdit] = useState({
    item: {},
    isEdit: false,
  });
  const [input, setInput] = useState({
    id: "",
    name: "",
    number: "",
    designation: "",
    address: "",
  });

  const [tableList, setTableList] = useState([]);

  useEffect(() => {
    fetchDetails();
  }, []);

  const fetchDetails = async () => {
    const response = await fetch(`/employee`);
    const data = await response.json();
    setTableList(data);
  };

  const handleInputChange = (e) => {
    //const name = e.target.name
    //const value = e.target.value
    const { name, value } = e.target;

    setInput({
      ...input,
      [name]: value,
    });
  };

  // add a record
  const handleSubmit = async () => {
    if (edit.isEdit === true) {
      update(edit.item.id, input);
    } else {
      const response = await fetch(`/employee`, {
        method: "POST",
        headers: {
          "content-Type": "application/json",
        },
        body: JSON.stringify(input),
      });
      console.log(input);
      const data = await response.json();

      setTableList([...tableList, data]);
      setInput({ id: "", name: "", number: "", designation: "", address: "" });
    }
  };

  //Delete a Recored
  const handleDelete = async (id) => {
    if (window.confirm("are you sure? You want to delete this record?"))
      await fetch(`/employee/${id}`, {
        method: "DELETE",
        headers: {
          "content-Type": "application/json",
        },
      });
    setTableList(tableList.filter((user) => user.id !== id));
  };

  /* const handleEdit = (id) => {
    const arr = tableList.filter((user) => user.id === id);
    setInput({
      id: arr[0].id,
      name: arr[0].name,
      number: arr[0].number,
      designation: arr[0].designation,
      address: arr[0].address,
    });
  };*/

  // set item to be update
  const handleEdit = (item) => {
    setEdit({
      item,
      isEdit: true,
    });
  };
  useEffect(() => {
    if (edit.isEdit === true) {
      setInput(edit.item);
    }
  }, [edit]);

  // Update a record
  const update = async (id, updItem) => {
    const response = await fetch(`/employee/${id}`, {
      method: "PUT",
      headers: {
        "content-Type": "application/json",
      },
      body: JSON.stringify(updItem),
    });
    console.log(input);
    const data = await response.json();

    setTableList(
      tableList.map((item) => (item.id === id ? { ...item, ...data } : item))
    );
  };

  return (
    <EmpContext.Provider
      value={{
        input,
        tableList,
        edit,
        /*handleId,
        handleName,
        handleNumber,
        handleDesignation,
        handleAddress,*/
        handleInputChange,
        handleSubmit,
        handleDelete,
        handleEdit,
        update,
      }}
    >
      {children}
    </EmpContext.Provider>
  );
};

export default EmpContext;
