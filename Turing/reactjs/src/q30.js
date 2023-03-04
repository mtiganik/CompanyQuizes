import React from 'react'

const userInfo = {
    name:"John",
    phone:"53543543",
    address:{
        present:{
            country:"Estonia",
            city:"Tallinn"
        },
        permanent:{
            country:"Finland",
            city:"Helsinki"
        }
    }
}
function Q30() {
    const [profileInfo, setProfileInfo] = React.useState(userInfo)
    
    // // A So so working
    profileInfo.address.present.city = "Sydney"

    // // B Not working
    // const updateProfile = {
    //     ...profileInfo,
    //     address:{
    //         present:{
    //             city: "Sydney"
    //         }
    //     }
    // }
    // setProfileInfo(updateProfile)

    // //C
    // const updateProfile= {
    //     ...profileInfo,
    //     address:{
    //         ...profileInfo.address,
    //         present:{
    //             city: "Sydney"
    //         }
    //     }
    // }
    // setProfileInfo(updateProfile)

    // //D  Not working
    // setProfileInfo((prevState) => ({
    //     ...prevState,
    //     address:{
    //         ...prevState.address,
    //         present:{
    //             ...prevState.present,
    //             city:"Sydney"
    //         }
    //     }
    // }))

    // //E  Not working
    // setProfileInfo((prevState) => ({
    //     ...prevState,
    //     address:{
    //         ...prevState.address,
    //         present:{
    //             city:"Sydney"
    //         }
    //     }
    // }))

    console.log(profileInfo)

    return(
        <p>Hello</p>
    )

}

export default Q30;