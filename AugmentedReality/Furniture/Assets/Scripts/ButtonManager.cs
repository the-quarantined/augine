using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
public class ButtonManager : MonoBehaviour
{
    // Start is called before the first frame update
    private Button btn;
    public GameObject furniture;
    void Start()
    {
        btn= GetComponent<Button>();
        btn.onClick.AddListener(SelectObject);
    }

    // Update is called once per frame
    void Update()
    {
        
    }
 
    void SelectObject(){
        DataHandler.Instance.furniture = furniture; 
    }
}
