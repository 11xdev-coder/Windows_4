using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Linq;

public class UserInput : MonoBehaviour
{
    public GameObject slot1;
    private Solitaire solitaire;
    private float timer;
    private float doubleClickTime = 0.3f;
    private int clickCount = 0;


    // Start is called before the first frame update
    void Start()
    {
        solitaire = FindObjectOfType<Solitaire>();
        slot1 = this.gameObject;
    }

    // Update is called once per frame
    void Update()
    {
        if (clickCount == 1)
        {
            timer += Time.deltaTime;
        }
        if (clickCount == 3)
        {
            timer = 0;
            clickCount = 1;
        }
        if (timer > doubleClickTime)
        {
            timer = 0;
            clickCount = 0;
        }

        GetMouseClick();
    }

    void GetMouseClick()
    {
        if (Input.GetMouseButtonDown(0))
        {
            clickCount++;

            Vector3 mousePosition = Camera.main.ScreenToWorldPoint(new Vector3(Input.mousePosition.x, Input.mousePosition.y, -10));
            RaycastHit2D hit = Physics2D.Raycast(Camera.main.ScreenToWorldPoint(Input.mousePosition), Vector2.zero);
            if (hit)
            {
                // what has been hit? Deck/Card/EmptySlot...
                if (hit.collider.CompareTag("Deck"))
                {
                    //clicked deck
                    Deck();
                }
                else if (hit.collider.CompareTag("Card"))
                {
                    // clicked card
                    Card(hit.collider.gameObject);
                }
                else if (hit.collider.CompareTag("Top"))
                {
                    // clicked top
                    Top(hit.collider.gameObject);
                }
                else if (hit.collider.CompareTag("Bottom"))
                {
                    // clicked bottom
                    Bottom(hit.collider.gameObject);
                }
            }
        }
    }

    void Deck()
    {
        // deck click actions
        print("Clicked on deck");
        solitaire.DealFromDeck();
        slot1 = this.gameObject;

    }
    void Card(GameObject selected)
    {
        // card click actions
        print("Clicked on Card");

        if (!selected.GetComponent<Selectable>().faceUp) // if the card clicked on is facedown
        {
            if (!Blocked(selected)) // if the card clicked on is not blocked
            {
                // flip it over
                selected.GetComponent<Selectable>().faceUp = true;
                slot1 = this.gameObject;
            }

        }
        else if (selected.GetComponent<Selectable>().inDeckPile) // if the card clicked on is in the deck pile with the trips
        {
            // if it is not blocked
            if (!Blocked(selected))
            {
                if (slot1 == selected) // if the same card is clicked twice
                {
                    if (DoubleClick())
                    {
                        // attempt auto stack
                        AutoStack(selected);
                    }
                }
                else
                {
                    slot1 = selected;
                }                
            }

        }
        else
        {

            // if the card is face up
            // if there is no card currently selected
            // select the card

            if (slot1 == this.gameObject) // not null because we pass in this gameObject instead
            {
                slot1 = selected;
            }

            // if there is already a card selected (and it is not the same card)
            else if (slot1 != selected)
            {
                // if the new card is eligable to stack on the old card
                if (Stackable(selected))
                {
                    Stack(selected);
                }
                else
                {
                    // select the new card
                    slot1 = selected;
                }
            }

            else if (slot1 == selected) // if the same card is clicked twice
            {
                if (DoubleClick())
                {
                    // attempt auto stack
                    AutoStack(selected);
                }
            }


        }
    }
    void Top(GameObject selected)
    {
        // top click actions
        print("Clicked on Top");
        if (slot1.CompareTag("Card"))
        {
            // if the card is an ace and the empty slot is top then stack
            if (slot1.GetComponent<Selectable>().value == 1)
            {
                Stack(selected);
            }

        }


    }
    void Bottom(GameObject selected)
    {
        // bottom click actions
        print("Clicked on Bottom");
        // if the card is a king and the empty slot is bottom then stack

        if (slot1.CompareTag("Card"))
        {
            if (slot1.GetComponent<Selectable>().value == 13)
            {
                Stack(selected);
            }
        }



    }

    bool Stackable(GameObject selected)
    {
        Selectable s1 = slot1.GetComponent<Selectable>();
        Selectable s2 = selected.GetComponent<Selectable>();
        // compare them to see if they stack

        if (!s2.inDeckPile)
        {
            if (s2.top) // if in the top pile must stack suited Ace to King
            {
                if (s1.suit == s2.suit || (s1.value == 1 && s2.suit == null))
                {
                    if (s1.value == s2.value + 1)
                    {
                        return true;
                    }
                }
                else
                {
                    return false;
                }
            }
            else  // if in the bottom pile must stack alternate colours King to Ace
            {
                if (s1.value == s2.value - 1)
                {
                    bool card1Red = true;
                    bool card2Red = true;

                    if (s1.suit == "C" || s1.suit == "S")
                    {
                        card1Red = false;
                    }

                    if (s2.suit == "C" || s2.suit == "S")
                    {
                        card2Red = false;
                    }

                    if (card1Red == card2Red)
                    {
                        print("Not stackable");
                        return false;
                    }
                    else
                    {
                        print("Stackable");
                        return true;
                    }
                }
            }
        }
        return false;
    }

    void Stack(GameObject selected)
    {
        // if on top of king or empty bottom stack the cards in place
        // else stack the cards with a negative y offset

        Selectable s1 = slot1.GetComponent<Selectable>();
        Selectable s2 = selected.GetComponent<Selectable>();
        float yOffset = 0.3f;

        if (s2.top || (!s2.top && s1.value == 13))
        {
            yOffset = 0;
        }

        slot1.transform.position = new Vector3(selected.transform.position.x, selected.transform.position.y - yOffset, selected.transform.position.z - 0.01f);
        slot1.transform.parent = selected.transform; // this makes the children move with the parents

        if (s1.inDeckPile) // removes the cards from the top pile to prevent duplicate cards
        {
            solitaire.tripsOnDisplay.Remove(slot1.name);
        }
        else if (s1.top && s2.top && s1.value == 1) // allows movement of cards between top spots
        {
            solitaire.topPos[s1.row].GetComponent<Selectable>().value = 0;
            solitaire.topPos[s1.row].GetComponent<Selectable>().suit = null;
        }
        else if (s1.top) // keeps track of the current value of the top decks as a card has been removed
        {
            solitaire.topPos[s1.row].GetComponent<Selectable>().value = s1.value - 1;
        }
        else // removes the card string from the appropriate bottom list
        {
            solitaire.bottoms[s1.row].Remove(slot1.name);
        }

        s1.inDeckPile = false; // you cannot add cards to the trips pile so this is always fine
        s1.row = s2.row;

        if (s2.top) // moves a card to the top and assigns the top's value and suit
        {
            solitaire.topPos[s1.row].GetComponent<Selectable>().value = s1.value;
            solitaire.topPos[s1.row].GetComponent<Selectable>().suit = s1.suit;
            s1.top = true;
        }
        else
        {
            s1.top = false;
        }

        // after completing move reset slot1 to be essentially null as being null will break the logic
        slot1 = this.gameObject;

    }

    bool Blocked(GameObject selected)
    {
        Selectable s2 = selected.GetComponent<Selectable>();
        if (s2.inDeckPile == true)
        {
            if (s2.name == solitaire.tripsOnDisplay.Last()) // if it is the last trip it is not blocked
            {
                return false;
            }
            else
            {
                print(s2.name + " is blocked by " + solitaire.tripsOnDisplay.Last());
                return true;
            }
        }
        else
        {
            if (s2.name == solitaire.bottoms[s2.row].Last()) // check if it is the bottom card
            {
                return false;
            }
            else
            {
                return true;
            }
        }
    }

    bool DoubleClick()
    {
        if (timer < doubleClickTime && clickCount == 2)
        {
            print("Double Click");
            return true;
        }
        else
        {
            return false;
        }
    }

    void AutoStack(GameObject selected)
    {
        for (int i = 0; i < solitaire.topPos.Length; i++)
        {
            Selectable stack = solitaire.topPos[i].GetComponent<Selectable>();
            if (selected.GetComponent<Selectable>().value == 1) // if it is an Ace
            {
                if (solitaire.topPos[i].GetComponent<Selectable>().value == 0) // and the top position is empty
                {
                    slot1 = selected;
                    Stack(stack.gameObject); // stack the ace up top
                    break;                  // in the first empty position found
                }
            }
            else
            {
                if ((solitaire.topPos[i].GetComponent<Selectable>().suit == slot1.GetComponent<Selectable>().suit) && (solitaire.topPos[i].GetComponent<Selectable>().value == slot1.GetComponent<Selectable>().value - 1))
                {
                    // if it is the last card (if it has no children)
                    if (HasNoChildren(slot1))
                    {
                        slot1 = selected;
                        // find a top spot that matches the conditions for auto stacking if it exists
                        string lastCardname = stack.suit + stack.value.ToString();
                        if (stack.value == 1)
                        {
                            lastCardname = stack.suit + "A";
                        }
                        if (stack.value == 11)
                        {
                            lastCardname = stack.suit + "J";
                        }
                        if (stack.value == 12)
                        {
                            lastCardname = stack.suit + "Q";
                        }
                        if (stack.value == 13)
                        {
                            lastCardname = stack.suit + "K";
                        }
                        GameObject lastCard = GameObject.Find(lastCardname);
                        Stack(lastCard);
                        break;
                    }
                }
            }



        }
    }

    bool HasNoChildren(GameObject card)
    {
        int i = 0;
        foreach (Transform child in card.transform)
        {
            i++;
        }
        if (i == 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }

}
