import React,{useState} from 'react'

function UpdateUser({name2, email2, description2}) {
    const [formData, setFormData] = useState ({
        name: name2,
        email: email2,
        description: description2
    })
  return (
    <div>UpdateUser</div>
  )
}

export default UpdateUser